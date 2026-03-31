#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全局配置中心 - 支持环境变量覆盖
"""

import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class APIConfig:
    """智谱 API 配置"""
    api_key: str = field(default_factory=lambda: os.getenv("ZHIPU_API_KEY", ""))
    api_base: str = "https://open.bigmodel.cn/api/paas/v4"
    model: str = "glm-4.7-flash"  # ✅ 正确模型名
    timeout: int = 120
    max_retries: int = 3
    retry_delay: float = 2.0
    
    # 生成参数
    temperature: float = 0.7
    top_p: float = 0.95
    max_tokens: int = 4096
    
    def __post_init__(self):
        if not self.api_key:
            raise ValueError("ZHIPU_API_KEY 未设置！请通过环境变量或配置文件提供")


@dataclass
class ChunkConfig:
    """文档分块配置"""
    min_tokens: int = 2000      # 最小块大小
    max_tokens: int = 5000      # 最大块大小
    overlap_ratio: float = 0.1  # 块重叠比例 (10%)
    # Token 估算：中文≈字符数/2.5, 英文≈字符数/4
    chars_per_token_zh: float = 2.5
    chars_per_token_en: float = 4.0


@dataclass
class HistoryConfig:
    """滑动历史配置"""
    window_size: int = 5  # 保留最近 5 轮关键对话
    summary_max_length: int = 500  # 关键内容总结最大长度


@dataclass
class PathConfig:
    """路径配置"""
    input_dir: Path = Path("./markdown_files")          # MD 输入目录
    output_dir: Path = Path("./afsim_dataset")          # 数据集输出目录
    progress_file: Path = field(default_factory=lambda: Path("./afsim_dataset/progress.json"))  # 进度文件
    log_file: Path = field(default_factory=lambda: Path("./afsim_dataset/build.log"))  # 日志文件
    test_output_dir: Path = field(default_factory=lambda: Path("./afsim_dataset/test"))  # 测试输出
    
    def __post_init__(self):
        # 确保目录存在
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.test_output_dir.mkdir(parents=True, exist_ok=True)


@dataclass
class Config:
    """全局配置聚合"""
    api: APIConfig = field(default_factory=APIConfig)
    chunk: ChunkConfig = field(default_factory=ChunkConfig)
    history: HistoryConfig = field(default_factory=HistoryConfig)
    paths: PathConfig = field(default_factory=PathConfig)
    
    # 系统提示词 (Alpaca 格式)
    system_prompt: str = """你是一个专业的 SFT 微调数据集生成器，专门用于构建 AFSIM (Advanced Framework for Simulation, Integration and Modeling) 想定脚本开发与知识问答的训练数据。

你的任务是基于用户提供的 AFSIM 使用手册内容切片，生成高质量的微调训练样本。

**输出要求：**
1. 必须输出严格的 JSON 数组格式，不要有任何额外文字、解释或 Markdown 标记
2. 每个样本遵循 Alpaca 格式：{"instruction": "问题/指令", "input": "可选上下文", "output": "详细回答"}
3. 指令要多样化：概念解释、语法查询、代码生成、故障排查、场景设计等
4. 回答要准确、完整，基于提供的手册内容，代码部分保持原始格式
5. 如果材料中有示例代码，必须保留并可运行
6. 根据内容长度，尽可能生成 5-15 条高质量样本

**禁止行为：**
- 不要输出"好的"、"以下是"等引导语
- 不要添加```json```标记
- 不要解释你的生成过程
- 不要生成与 AFSIM 无关的内容

现在，请基于以下手册内容生成数据集："""


# 全局配置实例
config = Config()


def reload_from_env():
    """从环境变量重新加载配置（用于测试）"""
    if os.getenv("ZHIPU_API_KEY"):
        config.api.api_key = os.getenv("ZHIPU_API_KEY")
    if os.getenv("INPUT_DIR"):
        config.paths.input_dir = Path(os.getenv("INPUT_DIR"))
    if os.getenv("OUTPUT_DIR"):
        config.paths.output_dir = Path(os.getenv("OUTPUT_DIR"))