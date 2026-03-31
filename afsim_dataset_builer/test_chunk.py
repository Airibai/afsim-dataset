#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 1: 单文件分块测试 + 可视化输出

用法：
  python test_chunk.py --file path/to/file.md
  python test_chunk.py --dir ./markdown_files --limit 3
"""

import argparse
import json
from pathlib import Path
import sys

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from config import config, reload_from_env
from chunker import DocumentChunker, Chunk
from token_utils import estimate_tokens
from logger import logger


def visualize_chunk(chunk: Chunk, max_preview: int = 300):
    """可视化输出单个块信息"""
    print(f"\n{'='*70}")
    print(f"📦 块 #{chunk.chunk_index+1}/{chunk.total_chunks}")
    print(f"📄 文件：{chunk.filename}")
    print(f"📍 位置：字符 [{chunk.char_start}:{chunk.char_end}]")
    print(f"🔢 Token 估算：{chunk.token_estimate}")
    print(f"{'-'*70}")
    
    # 内容预览
    preview = chunk.content[:max_preview]
    if len(chunk.content) > max_preview:
        preview += "\n...(省略)"
    
    print("📝 内容预览：")
    print(preview)
    print(f"{'='*70}")


def test_single_file(filepath: Path):
    """测试单个文件分块"""
    print(f"🧪 测试分块：{filepath.name}")
    print(f"📊 配置：min={config.chunk.min_tokens}, max={config.chunk.max_tokens} tokens")
    
    chunker = DocumentChunker()
    chunks = chunker.split_file(filepath)
    
    if not chunks:
        print("❌ 未生成任何块")
        return
    
    print(f"\n✅ 成功分块：{len(chunks)} 块")
    
    # 输出统计
    tokens_list = [c.token_estimate for c in chunks]
    print(f"📈 Token 分布：min={min(tokens_list)}, max={max(tokens_list)}, avg={sum(tokens_list)/len(tokens_list):.0f}")
    
    # 可视化前 3 块
    for chunk in chunks[:3]:
        visualize_chunk(chunk)
    
    # 保存分块结果（测试用）
    output = config.paths.test_output_dir / f"{filepath.stem}_chunks.json"
    with open(output, 'w', encoding='utf-8') as f:
        json.dump([c.to_dict() for c in chunks], f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 分块元数据已保存：{output}")
    print(f"💡 提示：完整内容可在代码中通过 chunk.content 访问")


def test_directory(input_dir: Path, limit: int = None):
    """测试目录下多个文件"""
    chunker = DocumentChunker()
    md_files = sorted(input_dir.glob("*.md"))
    
    if limit:
        md_files = md_files[:limit]
        print(f"📋 限制处理前 {limit} 个文件")
    
    total_chunks = 0
    for filepath in md_files:
        chunks = chunker.split_file(filepath)
        total_chunks += len(chunks)
        # 只可视化第一个文件的第一个块
        if filepath == md_files[0] and chunks:
            visualize_chunk(chunks[0])
    
    print(f"\n📊 批量测试完成：{len(md_files)} 文件 → {total_chunks} 块")


def main():
    parser = argparse.ArgumentParser(description="测试文档分块功能")
    parser.add_argument("-f", "--file", type=Path, help="测试单个 MD 文件")
    parser.add_argument("-d", "--dir", type=Path, default=config.paths.input_dir, 
                       help="测试目录（默认：input_dir）")
    parser.add_argument("-l", "--limit", type=int, help="目录模式下限制文件数")
    parser.add_argument("--env", action="store_true", help="从环境变量重载配置")
    
    args = parser.parse_args()
    
    # 重载配置（如果需要）
    if args.env:
        reload_from_env()
        logger.info("🔄 已从环境变量重载配置")
    
    # 执行测试
    if args.file:
        if not args.file.exists():
            print(f"❌ 文件不存在：{args.file}")
            return
        test_single_file(args.file)
    else:
        test_directory(args.dir, args.limit)
    
    print(f"\n✅ 测试完成！")


if __name__ == "__main__":
    main()