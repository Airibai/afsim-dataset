#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智谱清言 GLM-4-Flash 流式对话客户端
需求 1: 控制台输入问题 → 流式输出回答
"""

import os
import sys
import json
import requests
from typing import List, Optional

# ==================== 配置区域 ====================
CONFIG = {
    # 🔑 API 配置
    "api_key": os.getenv("ZHIPU_API_KEY", "1adfcaebe6364569974ea2f2260b0617.sWy8LvrAlXIABNPx"),  # 优先从环境变量读取
    "api_base": "https://open.bigmodel.cn/api/paas/v4",
    "model": "glm-4.7-flash",  # ✅ 正确的模型名称
    
    # ⚙️ 请求参数
    "temperature": 0.7,
    "top_p": 0.95,
    "max_tokens": 4096,
    
    # 🎨 输出样式
    "show_usage": True,        # 显示 Token 消耗
    "show_thinking": False,    # 是否显示思维链内容 (reasoning_content)
}
# ================================================


class GLMStreamClient:
    """智谱清言流式对话客户端"""
    
    def __init__(self, api_key: str, config: dict = None):
        """
        初始化客户端
        
        Args:
            api_key: 智谱开放平台 API Key
            config: 可选配置字典，会覆盖默认配置
        """
        self.api_key = api_key.strip()
        self.config = {**CONFIG, **(config or {})}
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
        
        # 对话历史（用于多轮对话）
        self.messages: List[dict] = []
        
        # 验证 API Key
        if not self.api_key or self.api_key == "your_api_key_here":
            print("⚠️  警告：API Key 未配置！")
            print("💡 获取方式：登录 https://open.bigmodel.cn → 个人中心 → API 管理")
            print("💡 或设置环境变量：export ZHIPU_API_KEY=your_key")
    
    def _build_payload(self, user_input: str) -> dict:
        """构建请求体"""
        # 添加用户消息
        self.messages.append({"role": "user", "content": user_input})
        
        return {
            "model": self.config["model"],
            "messages": self.messages,
            "stream": True,  # ✅ 启用流式输出
            "temperature": self.config["temperature"],
            "top_p": self.config["top_p"],
            "max_tokens": self.config["max_tokens"],
        }
    
    def _parse_sse_line(self, line: str) -> Optional[dict]:
        """
        解析 SSE 格式的单行数据
        
        SSE 格式: data: {"choices": [...]}
        结束标记: data: [DONE]
        """
        line = line.strip()
        if not line or line.startswith(":"):  # 跳过注释行
            return None
        if line == "data: [DONE]":  # 流结束标记
            return None
        if line.startswith("data: "):
            json_str = line[6:]  # 移除 "data: " 前缀
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                return None
        return None
    
    def chat_stream(self, user_input: str, callback=None):
        """
        发送流式对话请求
        
        Args:
            user_input: 用户输入的问题
            callback: 可选回调函数，每收到一个片段时调用 (content: str)
            
        Yields:
            str: 模型生成的文本片段
        """
        payload = self._build_payload(user_input)
        url = f"{self.config['api_base']}/chat/completions"
        
        full_response = ""
        usage_info = None
        
        try:
            # 发送流式请求 (stream=True)
            with self.session.post(url, json=payload, stream=True, timeout=120) as resp:
                resp.raise_for_status()
                
                # 逐行解析 SSE 响应
                for line in resp.iter_lines(decode_unicode=True):
                    chunk = self._parse_sse_line(line)
                    if not chunk:
                        continue
                    
                    # 提取内容
                    choices = chunk.get("choices", [])
                    if not choices:
                        continue
                    
                    delta = choices[0].get("delta", {})
                    content = delta.get("content", "")
                    
                    if content:
                        full_response += content
                        
                        # 调用回调（用于实时显示）
                        if callback:
                            callback(content)
                        else:
                            yield content
                    
                    # 收集用量信息（在最后一条消息中）
                    if "usage" in chunk:
                        usage_info = chunk["usage"]
                
                # 流结束：保存助手回复到历史
                if full_response:
                    self.messages.append({"role": "assistant", "content": full_response})
                
                # 返回用量信息
                if usage_info and self.config["show_usage"]:
                    yield f"\n\n[📊 Token: 输入 {usage_info.get('prompt_tokens', 0)} | 输出 {usage_info.get('completion_tokens', 0)} | 总计 {usage_info.get('total_tokens', 0)}]"
                    
        except requests.exceptions.Timeout:
            yield "\n\n❌ 请求超时，请检查网络连接"
        except requests.exceptions.ConnectionError:
            yield "\n\n❌ 连接失败，请检查网络或 API 地址"
        except requests.exceptions.HTTPError as e:
            error_msg = f"\n\n❌ HTTP 错误：{e}"
            if e.response is not None:
                try:
                    error_body = e.response.json()
                    error_msg += f" | {error_body.get('error', {}).get('message', '')}"
                except:
                    pass
            yield error_msg
        except Exception as e:
            yield f"\n\n❌ 未知错误：{type(e).__name__}: {e}"
    
    def clear_history(self):
        """清空对话历史"""
        self.messages = []
        print("🧹 对话历史已清空")
    
    def get_history(self) -> List[dict]:
        """获取当前对话历史"""
        return self.messages.copy()


def print_typewriter(text: str, end="", flush=True):
    """打字机效果输出（兼容中文）"""
    # 直接输出，不逐字打印（避免中文乱码和闪烁）
    print(text, end=end, flush=flush)


def interactive_mode():
    """交互式对话模式"""
    print("=" * 70)
    print("🤖 智谱清言 GLM-4-Flash 流式对话客户端")
    print("=" * 70)
    print("💡 输入问题后按回车，模型将流式输出回答")
    print("💡 输入 '/clear' 清空历史，输入 '/exit' 退出")
    print("💡 首次使用请配置 API Key：export ZHIPU_API_KEY=your_key")
    print("=" * 70)
    
    # 初始化客户端
    client = GLMStreamClient(CONFIG["api_key"])
    
    # 检查 API Key
    if client.api_key == "your_api_key_here":
        print("\n❌ 请先配置 API Key 后再使用！")
        return
    
    print(f"\n✅ 已加载模型：{CONFIG['model']}")
    print("-" * 70)
    
    # 主循环
    while True:
        try:
            # 获取用户输入
            user_input = input("\n👤 您：").strip()
            
            if not user_input:
                continue
            
            # 处理命令
            if user_input.lower() in ["/exit", "/quit", "退出"]:
                print("👋 再见！")
                break
            if user_input.lower() in ["/clear", "/reset", "清空"]:
                client.clear_history()
                continue
            if user_input.lower() in ["/help", "帮助"]:
                print("\n📋 可用命令:")
                print("  /clear  - 清空对话历史")
                print("  /exit   - 退出程序")
                print("  /help   - 显示此帮助")
                continue
            
            # 发送请求并流式输出
            print("🤖 助手：", end="", flush=True)
            
            for chunk in client.chat_stream(user_input, callback=print_typewriter):
                # callback 已经处理了输出，这里只需处理用量信息
                if chunk.startswith("\n\n[📊"):
                    print(chunk, flush=True)
            
            print()  # 换行
            
        except KeyboardInterrupt:
            print("\n\n⚠️  用户中断，输入 /exit 退出")
        except EOFError:
            print("\n👋 再见！")
            break


def single_query_mode(question: str):
    """单次查询模式（用于脚本调用）"""
    client = GLMStreamClient(CONFIG["api_key"])
    
    if client.api_key == "your_api_key_here":
        print("❌ 请配置 API Key")
        return
    
    print(f"🤖 提问：{question}\n")
    print("🤖 回答：", end="", flush=True)
    
    for chunk in client.chat_stream(question, callback=print_typewriter):
        if chunk.startswith("\n\n[📊"):
            print(chunk, flush=True)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="智谱清言 GLM-4-Flash 流式对话")
    parser.add_argument("-q", "--question", type=str, help="单次提问模式：直接输出答案后退出")
    parser.add_argument("-k", "--api-key", type=str, help="临时指定 API Key")
    
    args = parser.parse_args()
    
    # 临时覆盖 API Key
    if args.api_key:
        CONFIG["api_key"] = args.api_key
    
    # 运行模式
    if args.question:
        single_query_mode(args.question)
    else:
        interactive_mode()