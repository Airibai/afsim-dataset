#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
对话管理模块 - 处理请求/响应、提取关键内容、格式化输出
"""

import json
import re
import logging
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

from config import config
from glm_client import GLMClient

logger = logging.getLogger(__name__)


@dataclass
class ConversationRecord:
    """单轮对话记录"""
    timestamp: str
    filename: str
    chunk_index: int
    prompt: str  # 实际发送给模型的完整 prompt
    response_raw: str  # 模型原始响应
    datasets: List[dict]  # 解析后的数据集列表
    key_summary: str  # 关键内容总结
    question_summary: str  # 提问要点总结
    dataset_summary: str  # 数据集生成总结
    
    def to_dict(self) -> dict:
        """序列化（排除大字段）"""
        d = asdict(self)
        # 移除大字段，内容单独存储
        d.pop("prompt", None)
        d.pop("response_raw", None)
        return d
    
    def to_log_string(self) -> str:
        """生成日志摘要"""
        return (
            f"[{self.timestamp}] {self.filename}#{self.chunk_index} | "
            f"生成 {len(self.datasets)} 条数据 | "
            f"关键：{self.key_summary[:100]}..."
        )


class ConversationManager:
    """对话管理器"""
    
    def __init__(self, glm_client: GLMClient):
        self.client = glm_client
        self.system_prompt = config.system_prompt
    
    def build_prompt(self, chunk_content: str, history_summary: str = "") -> str:
        """
        构建完整 Prompt: [历史关键对话] + [System] + [当前切片]
        """
        parts = []
        
        # 1. 历史关键对话（如果有）
        if history_summary.strip():
            parts.append(f"【历史关键对话摘要】\n{history_summary}\n")
        
        # 2. System Prompt
        parts.append(f"【任务指令】\n{self.system_prompt}\n")
        
        # 3. 当前切片内容
        parts.append(f"【AFSIM 手册内容切片】\n{chunk_content}\n")
        
        # 4. 最终指令
        parts.append("请基于以上内容，生成符合要求的 JSON 数组数据集：")
        
        return "\n\n".join(parts)
    
    def parse_dataset_response(self, response: str) -> List[dict]:
        """
        解析模型响应，提取 JSON 数据集
        
        处理可能的格式：
        - 纯 JSON 数组: [...]
        - 带 Markdown: ```json [...] ```
        - 带前缀文字: "好的，以下是：\n[...]"
        """
        text = response.strip()
        
        # 尝试直接解析
        try:
            data = json.loads(text)
            if isinstance(data, list):
                return self._validate_datasets(data)
        except json.JSONDecodeError:
            pass
        
        # 尝试提取 JSON 部分
        # 模式 1: ```json [...] ```
        match = re.search(r'```(?:json)?\s*(\[.*?\])\s*```', text, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(1))
                if isinstance(data, list):
                    return self._validate_datasets(data)
            except:
                pass
        
        # 模式 2: 查找第一个 [ 和最后一个 ]
        start = text.find('[')
        end = text.rfind(']')
        if start != -1 and end != -1 and end > start:
            try:
                data = json.loads(text[start:end+1])
                if isinstance(data, list):
                    return self._validate_datasets(data)
            except:
                pass
        
        # 解析失败，返回空并记录警告
        logger.warning(f"⚠️  数据集解析失败，响应前 200 字符：{text[:200]}...")
        return []
    
    def _validate_datasets(self, datasets: List[dict]) -> List[dict]:
        """验证并清洗数据集条目"""
        valid = []
        for item in datasets:
            # 检查必要字段
            if not isinstance(item, dict):
                continue
            if "instruction" not in item or "output" not in item:
                continue
            # 基础长度检查
            if len(item.get("output", "")) < 50:
                continue
            # 添加到结果
            valid.append({
                "instruction": item["instruction"].strip(),
                "input": item.get("input", "").strip(),
                "output": item["output"].strip()
            })
        return valid
    
    def extract_key_content(self, prompt: str, response: str, datasets: List[dict]) -> Dict[str, str]:
        """
        调用 AI 提取关键内容总结
        
        Returns:
            dict: {
                "key_summary": "本次对话的关键提问信息总结",
                "question_summary": "用户提问要点",
                "dataset_summary": "生成的数据集总结"
            }
        """
        summary_prompt = f"""你是一个数据集质量评估专家。请基于以下对话内容，提取关键信息：

【用户提问要点】
{prompt[-1000:]}  # 取 prompt 末尾 1000 字符，通常是切片内容

【生成的数据集】(前 3 条示例)
{json.dumps(datasets[:3], ensure_ascii=False, indent=2)[:500]}

请用简洁的语言总结：
1. 本次提问的核心主题是什么？(20 字内)
2. 生成的数据集主要覆盖哪些知识点？(50 字内)
3. 数据质量如何？有什么特点？(30 字内)

输出格式（纯文本，无 JSON 标记）：
主题：...
知识点：...
质量：..."""
        
        try:
            result = self.client.chat([
                {"role": "system", "content": "你是一个专业的数据集评估助手，输出简洁的纯文本总结。"},
                {"role": "user", "content": summary_prompt}
            ])
            
            summary_text = result["content"]
            
            # 解析总结（简单规则）
            lines = summary_text.strip().split('\n')
            key_summary = ""
            question_summary = ""
            dataset_summary = ""
            
            for line in lines:
                if line.startswith("主题："):
                    question_summary = line[3:].strip()
                elif line.startswith("知识点："):
                    key_summary = line[4:].strip()
                elif line.startswith("质量："):
                    dataset_summary = line[3:].strip()
            
            # 兜底
            if not key_summary:
                key_summary = summary_text[:config.history.summary_max_length]
            if not question_summary:
                question_summary = "AFSIM 手册内容问答"
            if not dataset_summary:
                dataset_summary = f"生成 {len(datasets)} 条 Alpaca 格式数据"
            
            return {
                "key_summary": key_summary[:config.history.summary_max_length],
                "question_summary": question_summary[:100],
                "dataset_summary": dataset_summary[:100]
            }
            
        except Exception as e:
            logger.warning(f"⚠️  关键内容提取失败：{e}，使用默认总结")
            return {
                "key_summary": f"处理了 {len(datasets)} 条 AFSIM 相关数据",
                "question_summary": "AFSIM 手册内容",
                "dataset_summary": f"生成 {len(datasets)} 条训练样本"
            }
    
    def process_chunk(self, chunk, history_summary: str = "") -> Optional[ConversationRecord]:
        """
        处理单个文本块：调用 API → 解析响应 → 提取关键内容
        
        Returns:
            ConversationRecord 或 None (失败时)
        """
        logger.info(f"🔄 处理块：{chunk.filename}#{chunk.chunk_index+1}/{chunk.total_chunks}")
        
        # 1. 构建 Prompt
        prompt = self.build_prompt(chunk.content, history_summary)
        
        # 2. 调用 API (流式)
        logger.debug(f"📡 发送请求 (~{chunk.token_estimate} tokens)")
        response_parts = []
        
        try:
            messages = [{"role": "user", "content": prompt}]
            for part in self.client.chat_stream(messages):
                response_parts.append(part)
                # 实时日志（每 200 字符打印一次进度）
                if len("".join(response_parts)) % 200 < len(part):
                    logger.debug(f"  → 已接收 {len(''.join(response_parts))} 字符...")
            
            response_raw = "".join(response_parts)
            
        except Exception as e:
            logger.error(f"❌ API 调用失败：{e}")
            return None
        
        # 3. 解析数据集
        datasets = self.parse_dataset_response(response_raw)
        logger.info(f"✅ 解析出 {len(datasets)} 条有效数据")
        
        if not datasets:
            logger.warning(f"⚠️  未生成有效数据，跳过关键内容提取")
            # 仍记录对话，但标记为空
            datasets = []
        
        # 4. 提取关键内容
        logger.debug("🔍 提取关键内容...")
        key_contents = self.extract_key_content(prompt, response_raw, datasets)
        
        # 5. 构建记录
        record = ConversationRecord(
            timestamp=datetime.now().isoformat(),
            filename=chunk.filename,
            chunk_index=chunk.chunk_index,
            prompt=prompt,  # 完整 prompt 用于调试
            response_raw=response_raw,
            datasets=datasets,
            **key_contents
        )
        
        logger.info(record.to_log_string())
        return record