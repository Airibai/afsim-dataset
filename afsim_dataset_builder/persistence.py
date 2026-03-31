#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
持久化模块 - 进度/对话/历史 的读写管理
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

from config import config
from chunker import Chunk
from conversation import ConversationRecord
from sliding_history import SlidingHistory, HistoryEntry

logger = logging.getLogger(__name__)


class ProgressManager:
    """进度管理器 - 记录每个文件的处理状态"""
    
    def __init__(self, progress_file: Path = None):
        self.progress_file = progress_file or config.paths.progress_file
        self.progress: Dict[str, dict] = {}  # filename -> {last_chunk, processed_chunks, history}
        self._load()
    
    def _load(self):
        """从文件加载进度"""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    self.progress = json.load(f)
                logger.info(f"📥 加载进度：{len(self.progress)} 个文件")
            except Exception as e:
                logger.warning(f"⚠️  进度文件加载失败：{e}，从头开始")
                self.progress = {}
        else:
            logger.info("🆕 新任务，无历史进度")
    
    def _save(self):
        """保存进度到文件"""
        try:
            self.progress_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.progress_file, 'w', encoding='utf-8') as f:
                json.dump(self.progress, f, ensure_ascii=False, indent=2)
            logger.debug(f"💾 进度已保存：{self.progress_file}")
        except Exception as e:
            logger.error(f"❌ 保存进度失败：{e}")
    
    def get_file_progress(self, filename: str) -> dict:
        """获取单个文件的进度"""
        return self.progress.get(filename, {
            "last_chunk_index": -1,
            "processed_chunks": [],
            "history": [],
            "last_updated": None
        })
    
    def update_chunk_progress(self, filename: str, chunk_index: int, 
                           history_entries: List[dict] = None):
        """更新某个块的处理进度"""
        if filename not in self.progress:
            self.progress[filename] = {
                "last_chunk_index": -1,
                "processed_chunks": [],
                "history": [],
                "total_chunks": 0
            }
        
        prog = self.progress[filename]
        prog["last_chunk_index"] = max(prog["last_chunk_index"], chunk_index)
        
        if chunk_index not in prog["processed_chunks"]:
            prog["processed_chunks"].append(chunk_index)
            prog["processed_chunks"].sort()
        
        # 更新历史（如果提供）
        if history_entries:
            prog["history"] = history_entries[-config.history.window_size:]  # 只保留最近
        
        prog["last_updated"] = datetime.now().isoformat()
        
        # 自动保存（每更新 5 次保存一次，平衡性能和安全性）
        if len(prog["processed_chunks"]) % 5 == 0:
            self._save()
    
    def is_chunk_processed(self, filename: str, chunk_index: int) -> bool:
        """检查某个块是否已处理"""
        prog = self.get_file_progress(filename)
        return chunk_index in prog["processed_chunks"]
    
    def get_pending_chunks(self, filename: str, total_chunks: int) -> List[int]:
        """获取待处理的块索引列表"""
        prog = self.get_file_progress(filename)
        processed = set(prog["processed_chunks"])
        return [i for i in range(total_chunks) if i not in processed]
    
    def get_file_history(self, filename: str) -> List[dict]:
        """获取文件的滑动历史"""
        return self.progress.get(filename, {}).get("history", [])
    
    def save_all(self):
        """强制保存所有进度"""
        self._save()
        logger.info("💾 进度已强制保存")
    
    def get_stats(self) -> dict:
        """获取整体进度统计"""
        total_files = len(self.progress)
        processed_chunks = sum(len(p.get("processed_chunks", [])) for p in self.progress.values())
        
        return {
            "total_files": total_files,
            "processed_chunks": processed_chunks,
            "progress_file": str(self.progress_file)
        }


class DatasetStorage:
    """数据集存储管理器"""
    
    def __init__(self, output_dir: Path = None):
        self.output_dir = output_dir or config.paths.output_dir
        self.dataset_file = self.output_dir / "afsim_sft_dataset.jsonl"
        self.raw_responses_dir = self.output_dir / "raw_responses"  # 调试用
        self.raw_responses_dir.mkdir(parents=True, exist_ok=True)
        
        self._count = 0
    
    def save_datasets(self, records: List[ConversationRecord], append: bool = True):
        """
        保存数据集到 JSONL 文件
        
        Args:
            records: 对话记录列表
            append: 是否追加模式（默认是）
        """
        mode = 'a' if append else 'w'
        
        with open(self.dataset_file, mode, encoding='utf-8') as f:
            for record in records:
                # 转换为标准 Alpaca 格式 + 元数据
                for dataset in record.datasets:
                    entry = {
                        "messages": [
                            {"role": "system", "content": config.system_prompt},
                            {"role": "user", "content": dataset["instruction"] + (" " + dataset["input"] if dataset["input"] else "")},
                            {"role": "assistant", "content": dataset["output"]}
                        ],
                        "metadata": {
                            "source_file": record.filename,
                            "chunk_index": record.chunk_index,
                            "generated_at": record.timestamp,
                            "key_summary": record.key_summary
                        }
                    }
                    f.write(json.dumps(entry, ensure_ascii=False) + '\n')
                    self._count += 1
        
        logger.info(f"💾 保存 {len(records)} 条记录 → {sum(len(r.datasets) for r in records)} 条数据 (累计 {self._count})")
    
    def save_raw_response(self, record: ConversationRecord):
        """保存原始响应（调试用）"""
        filepath = self.raw_responses_dir / f"{record.filename}.chunk{record.chunk_index}.txt"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"=== Prompt ===\n{record.prompt}\n\n")
            f.write(f"=== Response ===\n{record.response_raw}\n\n")
            f.write(f"=== Metadata ===\n{json.dumps(record.to_dict(), ensure_ascii=False, indent=2)}")
    
    def get_count(self) -> int:
        """获取已保存的数据条数"""
        if self.dataset_file.exists():
            with open(self.dataset_file, 'r', encoding='utf-8') as f:
                return sum(1 for _ in f)
        return 0