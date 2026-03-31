#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 2: 单次问答测试 + 响应验证

用法：
  # 交互式输入
  python test_single_query.py --interactive
  
  # 指定内容测试
  python test_single_query.py --content "ENTITY 命令的语法是什么？" --file test.md
  
  # 测试关键内容提取
  python test_single_query.py --test-summary
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from config import config, reload_from_env
from glm_client import GLMClient
from conversation import ConversationManager
from sliding_history import SlidingHistory, HistoryEntry
from logger import logger


def test_api_connection():
    """测试 API 连接和基础对话"""
    print("🔌 测试 API 连接...")
    
    client = GLMClient()
    
    try:
        # 简单测试请求
        messages = [{"role": "user", "content": "你好，请用一句话介绍你自己"}]
        result = client.chat(messages)
        
        print(f"✅ 连接成功！")
        print(f"🤖 回复：{result['content'][:100]}...")
        print(f"📊 用量：{result.get('usage', {})}")
        
        return True
        
    except Exception as e:
        print(f"❌ 连接失败：{e}")
        return False


def test_single_query(content: str, filename: str = "test.md", history_text: str = ""):
    """测试单次查询 + 数据集生成"""
    print(f"🧪 测试单次查询")
    print(f"📄 模拟文件：{filename}")
    print(f"📝 内容长度：{len(content)} 字符")
    
    client = GLMClient()
    manager = ConversationManager(client)
    
    # 构建 prompt
    prompt = manager.build_prompt(content, history_text)
    print(f"\n📡 发送请求...")
    
    # 调用 API
    response_parts = []
    try:
        messages = [{"role": "user", "content": prompt}]
        print("🤖 助手：", end="", flush=True)
        
        for part in client.chat_stream(messages):
            print(part, end="", flush=True)
            response_parts.append(part)
        
        print()  # 换行
        response_raw = "".join(response_parts)
        
    except Exception as e:
        print(f"\n❌ 请求失败：{e}")
        return
    
    # 解析数据集
    print(f"\n🔍 解析响应...")
    datasets = manager.parse_dataset_response(response_raw)
    print(f"✅ 解析出 {len(datasets)} 条有效数据")
    
    # 展示前 2 条
    for i, ds in enumerate(datasets[:2], 1):
        print(f"\n【数据#{i}】")
        print(f"问：{ds['instruction']}")
        print(f"答：{ds['output'][:200]}...")
    
    # 测试关键内容提取
    print(f"\n🔍 测试关键内容提取...")
    key_contents = manager.extract_key_content(prompt, response_raw, datasets)
    
    print(f"📋 提取结果：")
    print(f"  提问要点：{key_contents['question_summary']}")
    print(f"  知识点：{key_contents['key_summary']}")
    print(f"  数据总结：{key_contents['dataset_summary']}")
    
    # 保存测试输出
    output = {
        "timestamp": datetime.now().isoformat(),
        "filename": filename,
        "content_preview": content[:200],
        "response_preview": response_raw[:500],
        "datasets_count": len(datasets),
        "datasets_sample": datasets[:2],
        "key_contents": key_contents
    }
    
    output_file = config.paths.test_output_dir / "single_query_test.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 测试输出已保存：{output_file}")


def test_summary_extraction():
    """专门测试关键内容提取功能"""
    print("🧪 测试关键内容提取")
    
    client = GLMClient()
    manager = ConversationManager(client)
    
    # 模拟数据
    prompt = "【任务指令】\n..."  # 简化
    response_raw = '[{"instruction": "什么是 ENTITY 命令？", "output": "ENTITY 用于定义仿真实体..."}]'
    datasets = manager.parse_dataset_response(response_raw)
    
    print(f"📝 模拟输入：{len(datasets)} 条数据")
    
    key_contents = manager.extract_key_content(prompt, response_raw, datasets)
    
    print(f"✅ 提取结果：")
    for k, v in key_contents.items():
        print(f"  {k}: {v}")


def interactive_mode():
    """交互式测试模式"""
    print("🎮 进入交互式测试模式")
    print("💡 输入内容后按回车，输入 /exit 退出")
    
    client = GLMClient()
    manager = ConversationManager(client)
    history = SlidingHistory()
    
    while True:
        try:
            content = input("\n📝 输入手册内容片段 (或 /exit): ").strip()
            if not content:
                continue
            if content.lower() in ['/exit', '退出']:
                break
            
            # 获取历史摘要
            history_text = history.get_summary_text()
            
            # 处理
            record = manager.process_chunk(
                type('Chunk', (), {
                    "content": content,
                    "filename": "interactive_test",
                    "chunk_index": 0,
                    "total_chunks": 1,
                    "token_estimate": len(content) // 3
                })(),
                history_text
            )
            
            if record:
                # 展示结果
                print(f"\n✅ 生成 {len(record.datasets)} 条数据")
                if record.datasets:
                    print(f"📋 示例：{record.datasets[0]['instruction'][:50]}...")
                
                # 更新历史
                history.add_from_record(record)
                print(f"📊 历史窗口：{len(history.history)} 条")
            
        except KeyboardInterrupt:
            print("\n⚠️  中断")
            break
        except EOFError:
            break


def main():
    parser = argparse.ArgumentParser(description="测试单次问答功能")
    parser.add_argument("-i", "--interactive", action="store_true", help="交互式测试模式")
    parser.add_argument("-c", "--content", type=str, help="测试内容字符串")
    parser.add_argument("-f", "--file", type=Path, help="从文件读取测试内容")
    parser.add_argument("--test-summary", action="store_true", help="仅测试关键内容提取")
    parser.add_argument("--env", action="store_true", help="从环境变量重载配置")
    
    args = parser.parse_args()
    
    # 重载配置
    if args.env:
        reload_from_env()
        logger.info("🔄 已从环境变量重载配置")
    
    # 先测试连接
    if not test_api_connection():
        print("\n❌ API 连接失败，请检查配置后重试")
        return
    
    # 执行对应测试
    if args.test_summary:
        test_summary_extraction()
    elif args.interactive:
        interactive_mode()
    elif args.content or args.file:
        # 获取内容
        if args.file:
            with open(args.file, 'r', encoding='utf-8') as f:
                content = f.read()
            filename = args.file.name
        else:
            content = args.content
            filename = "manual_input"
        
        # 获取历史（测试用空历史）
        history_text = ""
        
        test_single_query(content, filename, history_text)
    else:
        # 默认：显示帮助
        parser.print_help()
    
    print(f"\n✅ 测试完成！")


if __name__ == "__main__":
    main()