#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
滑动窗口历史管理器 - 维护最近 5 轮关键对话摘要
"""

from collections import deque
from typing import List, Optional
from dataclasses import dataclass, asdict
import json
import logging

from config import config

logger = logging.getLogger(__name__)


@dataclass
class HistoryEntry:
    """单条历史摘要"""
    filename: str
    chunk_index: int
    question_summary: str  # 提问要点 (≤100 字)
    key_summary: str       # 知识点总结 (≤500 字)
    dataset_summary: str   # 数据生成总结 (≤100 字)
    
    def to_short_string(self) -> str:
        """生成紧凑的历史字符串（用于构建 prompt）"""
        return (
            f"[{self.filename}#{self.chunk_index+1}] "
            f"问题：{self.question_summary} | "
            f"知识：{self.key_summary} | "
            f"回答：{self.dataset_summary}"
        )


class SlidingHistory:
    """滑动窗口历史管理器"""
    
    def __init__(self, window_size: int = None):
        self.window_size = window_size or config.history.window_size
        self.history: deque[HistoryEntry] = deque(maxlen=self.window_size)
    
    def add(self, entry: HistoryEntry):
        """添加新条目（自动维护窗口大小）"""
        self.history.append(entry)
        logger.debug(f"📝 历史窗口：{len(self.history)}/{self.window_size} 条")
    
    def add_from_record(self, record):
        """从 ConversationRecord 创建并添加历史"""
        entry = HistoryEntry(
            filename=record.filename,
            chunk_index=record.chunk_index,
            question_summary=record.question_summary,
            key_summary=record.key_summary,
            dataset_summary=record.dataset_summary
        )
        self.add(entry)
    
    def get_summary_text(self) -> str:
        """
        获取历史摘要文本（用于构建 prompt）
        
        格式：
        【历史对话摘要】(最近 5 轮)
        1. [文件#块] 问：... | 知：... | 数：...
        2. ...
        """
        if not self.history:
            return ""
        
        lines = ["【历史对话摘要】(最近 5 轮)"]
        for idx, entry in enumerate(self.history, 1):
            lines.append(f"{idx}. {entry.to_short_string()}")
        
        return "\n".join(lines)
    
    def to_dict_list(self) -> List[dict]:
        """序列化用于持久化"""
        return [asdict(e) for e in self.history]
    
    def from_dict_list(self, data: List[dict]):
        """从持久化数据恢复"""
        self.history.clear()
        for item in data:
            entry = HistoryEntry(**item)
            self.history.append(entry)
        logger.info(f"📥 恢复历史：{len(self.history)} 条")
    
    def clear(self):
        """清空历史"""
        self.history.clear()
        logger.debug("🧹 历史窗口已清空")