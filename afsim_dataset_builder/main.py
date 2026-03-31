#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AFSIM 微调数据集构建器 - 主入口

功能：
1. 加载进度，支持断点续传
2. 遍历 MD 文件 → 分块 → 调用 API → 生成数据集
3. 维护滑动历史，持久化进度
4. 合并输出最终 JSONL 数据集

用法：
  # 首次运行（从头开始）
  python main.py
  
  # 断点续传（自动检测进度）
  python main.py
  
  # 指定目录
  python main.py --input ./my_md_files
  
  # 测试模式（只处理 1 个文件）
  python main.py --limit 1
"""

import argparse
import sys
import json
from pathlib import Path
from datetime import datetime

# 添加项目根目录
sys.path.insert(0, str(Path(__file__).parent))

from config import config, reload_from_env
from logger import logger, setup_logger
from chunker import DocumentChunker
from glm_client import GLMClient
from conversation import ConversationManager, ConversationRecord
from sliding_history import SlidingHistory, HistoryEntry
from persistence import ProgressManager, DatasetStorage


class DatasetBuilder:
    """主构建器 - 协调各模块完成数据集生成"""
    
    def __init__(self):
        # 初始化组件
        self.chunker = DocumentChunker()
        self.client = GLMClient()
        self.manager = ConversationManager(self.client)
        self.progress = ProgressManager()
        self.storage = DatasetStorage()
        
        # 全局滑动历史（跨文件）
        self.global_history = SlidingHistory()
        
        logger.info("🚀 AFSIM 数据集构建器初始化完成")
    
    def _load_global_history(self):
        """从进度文件恢复全局历史（取最后一个文件的最新历史）"""
        # 简单策略：取进度中最后更新的文件的历史
        latest_file = None
        latest_time = ""
        
        for filename, prog in self.progress.progress.items():
            updated = prog.get("last_updated", "")
            if updated > latest_time:
                latest_time = updated
                latest_file = filename
        
        if latest_file:
            history_data = self.progress.get_file_history(latest_file)
            if history_data:
                self.global_history.from_dict_list(history_data)
                logger.info(f"📥 恢复全局历史：{len(self.global_history.history)} 条 (来自 {latest_file})")
    
    def _update_global_history(self, record: ConversationRecord):
        """更新全局滑动历史"""
        self.global_history.add_from_record(record)
        
        # 同时更新当前文件的进度历史
        history_entries = [h.__dict__ for h in self.global_history.history]
        self.progress.update_chunk_progress(
            record.filename, 
            record.chunk_index,
            history_entries
        )
    
    def process_file(self, filepath: Path) -> bool:
        """
        处理单个文件：分块 → 逐块调用 → 持久化
        
        Returns:
            bool: 是否成功完成
        """
        filename = filepath.name
        logger.info(f"\n{'='*60}")
        logger.info(f"📄 处理文件：{filename}")
        logger.info(f"{'='*60}")
        
        # 1. 分块
        chunks = self.chunker.split_file(filepath)
        if not chunks:
            logger.warning(f"⚠️  无有效块，跳过：{filename}")
            return True  # 不算失败
        
        # 2. 获取待处理块
        pending = self.progress.get_pending_chunks(filename, len(chunks))
        if not pending:
            logger.info(f"✅ 文件已完成：{filename} ({len(chunks)} 块)")
            return True
        
        logger.info(f"📋 待处理：{len(pending)}/{len(chunks)} 块")
        
        # 3. 恢复文件级历史
        file_history_data = self.progress.get_file_history(filename)
        file_history = SlidingHistory()
        if file_history_data:
            file_history.from_dict_list(file_history_data)
        
        # 4. 逐块处理
        processed_records = []
        
        for chunk_idx in pending:
            chunk = chunks[chunk_idx]
            
            # 检查是否已处理（双重确认）
            if self.progress.is_chunk_processed(filename, chunk_idx):
                logger.debug(f"⊘ 跳过已处理块：{filename}#{chunk_idx+1}")
                continue
            
            logger.info(f"\n🔄 块 {chunk_idx+1}/{len(chunks)}: {chunk.token_estimate} tokens")
            
            # 构建历史摘要：全局历史 + 文件历史
            history_parts = []
            if self.global_history.history:
                history_parts.append("【全局历史】\n" + self.global_history.get_summary_text())
            if file_history.history:
                history_parts.append("【文件历史】\n" + file_history.get_summary_text())
            history_text = "\n\n".join(history_parts) if history_parts else ""
            
            # 处理块
            record = self.manager.process_chunk(chunk, history_text)
            
            if not record:
                logger.error(f"❌ 块处理失败：{filename}#{chunk_idx+1}，记录错误并跳过")
                # 仍标记为已处理（避免无限重试）
                self.progress.update_chunk_progress(filename, chunk_idx)
                continue
            
            # 保存原始响应（调试）
            self.storage.save_raw_response(record)
            
            # 保存数据集
            if record.datasets:
                self.storage.save_datasets([record])
            
            # 更新历史
            file_history.add_from_record(record)
            self._update_global_history(record)
            
            # 记录
            processed_records.append(record)
            
            # 定期保存进度
            if (chunk_idx + 1) % 3 == 0:
                self.progress.save_all()
                logger.info(f"💾 进度已保存")
                
        
        # 5. 保存最终进度
        self.progress.save_all()
        
        # 6. 统计
        total_generated = sum(len(r.datasets) for r in processed_records)
        logger.info(f"✅ 文件完成：{filename}")
        logger.info(f"📊 生成 {len(processed_records)} 条记录 → {total_generated} 条数据")
        
        return True
    
    def run(self, limit_files: int = None):
        """
        主执行流程
        
        Args:
            limit_files: 限制处理的文件数（测试用）
        """
        logger.info("🎯 开始构建 AFSIM 微调数据集")
        logger.info(f"📁 输入：{config.paths.input_dir}")
        logger.info(f"📦 输出：{config.paths.output_dir}")
        logger.info(f"⚙️  配置：model={config.api.model}, tokens=[{config.chunk.min_tokens}, {config.chunk.max_tokens}]")
        
        # 恢复全局历史
        self._load_global_history()
        
        # 收集文件
        md_files = sorted(config.paths.input_dir.glob("*.md"))
        if not md_files:
            logger.error(f"❌ 未找到 MD 文件：{config.paths.input_dir}")
            return
        
        if limit_files:
            md_files = md_files[:limit_files]
            logger.info(f"📋 测试模式：限制处理 {limit_files} 个文件")
        
        logger.info(f"📊 待处理：{len(md_files)} 个文件")
        
        # 处理每个文件
        success_count = 0
        for idx, filepath in enumerate(md_files, 1):
            logger.info(f"\n{'#'*60}")
            logger.info(f"📁 文件进度：[{idx}/{len(md_files)}] {filepath.name}")
            logger.info(f"{'#'*60}")
            
            try:
                if self.process_file(filepath):
                    success_count += 1
            except KeyboardInterrupt:
                logger.warning("⚠️  用户中断，保存进度后退出")
                self.progress.save_all()
                break
            except Exception as e:
                logger.exception(f"❌ 文件处理异常：{filepath.name}: {e}")
                # 继续下一个文件
        
        # 最终统计
        self.progress.save_all()
        dataset_count = self.storage.get_count()
        api_stats = self.client.get_stats()
        
        logger.info(f"\n{'='*60}")
        logger.info("🎉 构建完成！")
        logger.info(f"{'='*60}")
        logger.info(f"✅ 成功处理：{success_count}/{len(md_files)} 文件")
        logger.info(f"📊 生成数据集：{dataset_count} 条")
        logger.info(f"🌐 API 调用：{api_stats['request_count']} 次")
        logger.info(f"🔢 消耗 Token: {api_stats['total_tokens']:,}")
        logger.info(f"💰 估算成本：¥{api_stats['estimated_cost_cny']:.2f}")
        logger.info(f"📦 输出文件：{self.storage.dataset_file}")
        logger.info(f"📋 进度文件：{self.progress.progress_file}")
        logger.info(f"{'='*60}")
        
        # 输出数据预览
        if dataset_count > 0:
            logger.info(f"\n📋 数据预览 (前 3 条):")
            with open(self.storage.dataset_file, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    if i >= 3:
                        break
                    entry = json.loads(line)
                    print(f"{i+1}. {entry['messages'][1]['content'][:60]}...")


def main():
    # 解析参数
    parser = argparse.ArgumentParser(description="AFSIM 微调数据集构建器")
    parser.add_argument("-i", "--input", type=Path, help="MD 文件输入目录")
    parser.add_argument("-o", "--output", type=Path, help="数据集输出目录")
    parser.add_argument("-l", "--limit", type=int, help="限制处理文件数（测试用）")
    parser.add_argument("--env", action="store_true", help="从环境变量重载配置")
    parser.add_argument("--reset", action="store_true", help="重置进度，从头开始")
    
    args = parser.parse_args()
    
    # 重载配置
    if args.env:
        reload_from_env()
        logger.info("🔄 已从环境变量重载配置")
    
    # 更新路径
    if args.input:
        config.paths.input_dir = args.input
    if args.output:
        config.paths.output_dir = args.output
        config.paths.progress_file = args.output / "progress.json"
        config.paths.log_file = args.output / "build.log"
        # 重新配置日志
        setup_logger(log_file=config.paths.log_file)
    
    # 重置进度
    if args.reset:
        if config.paths.progress_file.exists():
            config.paths.progress_file.unlink()
            logger.info("🗑️  进度文件已删除，将从头开始")
    
    # 检查 API Key
    if not config.api.api_key:
        logger.error("❌ ZHIPU_API_KEY 未配置！")
        logger.error("💡 请设置环境变量：export ZHIPU_API_KEY=sk-xxx")
        logger.error("💡 或编辑 config.py 直接填写")
        return
    
    # 运行构建
    builder = DatasetBuilder()
    builder.run(limit_files=args.limit)


if __name__ == "__main__":
    main()