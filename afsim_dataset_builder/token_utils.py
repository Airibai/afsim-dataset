#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Token 估算工具 - 无需外部依赖的轻量实现
基于字符统计的启发式估算（中文≈2.5 字符/Token, 英文≈4 字符/Token）
"""

import re
from config import config


def estimate_tokens(text: str) -> int:
    """
    估算文本的 Token 数量
    
    策略：
    - 中文字符：每 2.5 字符≈1 Token
    - 英文字符/数字：每 4 字符≈1 Token  
    - 代码/特殊符号：每 3 字符≈1 Token
    
    注意：这是估算值，与实际 tokenizer 可能有±15% 误差
    """
    if not text:
        return 0
    
    # 分类统计
    zh_chars = len(re.findall(r'[\u4e00-\u9fff]', text))  # 中文
    en_chars = len(re.findall(r'[a-zA-Z0-9]', text))       # 英文数字
    other_chars = len(text) - zh_chars - en_chars          # 其他（标点、代码符号等）
    
    # 加权计算
    tokens = (
        zh_chars / config.chunk.chars_per_token_zh +
        en_chars / config.chunk.chars_per_token_en +
        other_chars / 3.0  # 代码符号折中
    )
    
    return int(tokens)


def text_to_tokens(text: str) -> int:
    """别名，保持接口一致"""
    return estimate_tokens(text)


def truncate_to_tokens(text: str, max_tokens: int) -> str:
    """
    截断文本到指定 Token 数（保守估计，避免超限）
    
    策略：按字符比例截断，预留 10% 缓冲
    """
    if not text:
        return text
    
    current_tokens = estimate_tokens(text)
    if current_tokens <= max_tokens:
        return text
    
    # 计算截断比例（预留 10% 缓冲）
    ratio = (max_tokens * 0.9) / current_tokens
    truncate_len = max(100, int(len(text) * ratio))  # 至少保留 100 字符
    
    # 按段落截断，避免切断代码块
    truncated = text[:truncate_len]
    
    # 尝试在段落边界截断
    last_newline = truncated.rfind('\n\n')
    if last_newline > truncate_len * 0.8:  # 80% 位置后有段落结束
        truncated = truncated[:last_newline]
    
    return truncated + "\n\n...(内容截断)"


def calculate_chunk_boundaries(text: str, min_tokens: int, max_tokens: int, overlap_ratio: float) -> list[tuple]:
    """
    计算分块边界 [(start, end), ...]
    
    策略：
    1. 按段落/代码块边界切分，避免切断语义
    2. 块大小在 [min_tokens, max_tokens] 区间
    3. 相邻块重叠 overlap_ratio 保证上下文连续
    """
    if not text:
        return []
    
    chunks = []
    start = 0
    total_chars = len(text)
    
    while start < total_chars:
        # 估算当前起点到各位置的 token 数
        end = start
        tokens = 0
        
        # 逐步扩展直到达到 max_tokens
        while end < total_chars and tokens < max_tokens:
            # 每次扩展 100 字符（平衡精度和性能）
            next_end = min(end + 100, total_chars)
            segment = text[end:next_end]
            tokens += estimate_tokens(segment)
            end = next_end
        
        # 如果块太小且不是最后一块，继续扩展
        if tokens < min_tokens and end < total_chars:
            continue
        
        # 确保不超过最大限制
        if tokens > max_tokens:
            # 回退到上一个合理位置
            end = max(start + 100, end - 200)
        
        # 添加重叠（除了最后一块）
        overlap = 0
        if end < total_chars:
            overlap_chars = int((end - start) * overlap_ratio)
            # 在段落边界找重叠起点
            overlap_start = max(start, end - overlap_chars)
            # 调整到段落边界
            newline_pos = text.rfind('\n\n', start, overlap_start + 50)
            if newline_pos > start:
                overlap_start = newline_pos + 2
            chunks.append((start, overlap_start))
            start = overlap_start
        else:
            # 最后一块，无重叠
            chunks.append((start, end))
            break
    
    return chunks