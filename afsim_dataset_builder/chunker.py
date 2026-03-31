#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档分块器 - 将 MD 文件按 Token 数智能切分
"""

import re
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
import logging

from config import config
from token_utils import estimate_tokens, calculate_chunk_boundaries

logger = logging.getLogger(__name__)


@dataclass
class Chunk:
    """文本块数据结构"""
    content: str
    filename: str
    chunk_index: int
    total_chunks: int
    char_start: int
    char_end: int
    token_estimate: int
    
    def to_dict(self) -> dict:
        """序列化为字典（用于持久化）"""
        return {
            "filename": self.filename,
            "chunk_index": self.chunk_index,
            "total_chunks": self.total_chunks,
            "char_start": self.char_start,
            "char_end": self.char_end,
            "token_estimate": self.token_estimate,
            # content 单独存储，避免日志过大
        }
    
    def __repr__(self):
        return f"Chunk({self.filename}#{self.chunk_index}/{self.total_chunks}, {self.token_estimate} tokens)"


class DocumentChunker:
    """文档分块器"""
    
    def __init__(self, config_ref=None):
        self.cfg = config_ref or config
    
    def split_file(self, filepath: Path) -> List[Chunk]:
        """
        将单个 MD 文件分块
        
        Returns:
            List[Chunk]: 按顺序排列的文本块列表
        """
        logger.info(f"📄 分块处理：{filepath.name}")
        
        # 读取文件
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            logger.error(f"❌ 读取文件失败 {filepath}: {e}")
            return []
        
        if not content.strip():
            logger.warning(f"⚠️  文件为空：{filepath.name}")
            return []
        
        # 计算分块边界
        boundaries = calculate_chunk_boundaries(
            content,
            min_tokens=self.cfg.chunk.min_tokens,
            max_tokens=self.cfg.chunk.max_tokens,
            overlap_ratio=self.cfg.chunk.overlap_ratio
        )
        
        if not boundaries:
            logger.warning(f"⚠️  无法分块：{filepath.name} (内容太少？)")
            # 如果内容太少，整体作为一个块
            if estimate_tokens(content) > 0:
                return [Chunk(
                    content=content,
                    filename=filepath.name,
                    chunk_index=0,
                    total_chunks=1,
                    char_start=0,
                    char_end=len(content),
                    token_estimate=estimate_tokens(content)
                )]
            return []
        
        # 生成 Chunk 对象
        chunks = []
        for idx, (start, end) in enumerate(boundaries):
            chunk_content = content[start:end]
            chunk = Chunk(
                content=chunk_content,
                filename=filepath.name,
                chunk_index=idx,
                total_chunks=len(boundaries),
                char_start=start,
                char_end=end,
                token_estimate=estimate_tokens(chunk_content)
            )
            chunks.append(chunk)
            logger.debug(f"  ✓ 块 {idx+1}/{len(boundaries)}: {chunk.token_estimate} tokens, 字符 [{start}:{end}]")
        
        logger.info(f"✅ 分块完成：{filepath.name} → {len(chunks)} 块")
        return chunks
    
    def split_all(self, input_dir: Path, file_pattern: str = "*.md") -> List[Chunk]:
        """
        分块处理目录下所有匹配文件
        
        Returns:
            List[Chunk]: 所有文件的块，按文件名字典序排列
        """
        all_chunks = []
        md_files = sorted(input_dir.glob(file_pattern))
        
        logger.info(f"📁 扫描目录：{input_dir}，找到 {len(md_files)} 个 MD 文件")
        
        for filepath in md_files:
            chunks = self.split_file(filepath)
            all_chunks.extend(chunks)
        
        logger.info(f"📊 总计：{len(all_chunks)} 个文本块")
        return all_chunks