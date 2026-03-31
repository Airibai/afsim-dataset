# AFSIM 微调数据集构建器 - 完整实现方案

## 系统架构

┌─────────────────────────────────────────────────────────┐
│  📁 输入：63 个 AFSIM 手册 MD 文件                        │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│  🔧 核心模块                                              │
│  ├─ config.py          # 配置管理 (API Key/路径/参数)    │
│  ├─ token_utils.py     # Token 估算 (中文≈字符数/2.5)    │
│  ├─ chunker.py         # 文档分块 (2000-5000 tokens)    │
│  ├─ glm_client.py      # GLM API 客户端 (重试/流式)      │
│  ├─ conversation.py    # 对话管理 + 关键内容提取         │
│  ├─ sliding_history.py # 滑动窗口 (5 轮关键对话)         │
│  ├─ persistence.py     # 进度/对话持久化 (JSON)          │
│  └─ logger.py          # 结构化日志                      │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│  🧪 测试模块                                              │
│  ├─ test_chunk.py       # 单文件分块测试 + 可视化输出    │
│  └─ test_single_query.py # 单次问答测试 + 响应验证       │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│  🎯 主流程 (main.py)                                      │
│  1. 加载进度 → 2. 遍历文件 → 3. 分块 → 4. 调用 API        │
│  5. 提取关键内容 → 6. 更新滑动历史 → 7. 持久化 → 8. 合并  │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│  📦 输出：afsim_sft_dataset.jsonl + 进度文件 + 日志       │
└─────────────────────────────────────────────────────────┘

## 项目结构

afsim_dataset_builder/
├── config.py              # 配置中心
├── token_utils.py         # Token 估算工具
├── chunker.py             # 文档分块器
├── glm_client.py          # GLM API 客户端
├── conversation.py        # 对话管理 + 关键内容提取
├── sliding_history.py     # 滑动窗口历史
├── persistence.py         # 进度/数据持久化
├── logger.py              # 日志配置
├── test_chunk.py          # 分块测试脚本
├── test_single_query.py   # 单次问答测试脚本
├── main.py                # 主入口
├── requirements.txt       # 依赖列表
├── .env.example           # 环境变量模板
└── README.md              # 使用文档

# 🧪 使用流程

## 环境准备

1. 创建虚拟环境
python -m venv afsim_env
source afsim_env/bin/activate  # Linux/Mac
或 afsim_env\Scripts\activate  # Windows

2. 安装依赖
pip install -r requirements.txt

3. 配置 API Key
export ZHIPU_API_KEY="sk-xxxxxx"  # Linux/Mac
或 $env:ZHIPU_API_KEY="sk-xxxxxx"  # PowerShell

## 测试分块功能

1. 测试单个文件分块 + 可视化
python test_chunk.py --file ./markdown_files/AFSIM2.9 参考手册-v1.1_1-40.md

2. 测试目录（前 3 个文件）
python test_chunk.py --dir ./markdown_files --limit 3

预期输出：看到分块统计 + 内容预览 + 保存的 JSON 元数据

## 测试单次问答

1. 测试 API 连接 + 简单问答
python test_single_query.py

2. 交互式测试
python test_single_query.py --interactive

3. 指定内容测试
python test_single_query.py --content "ENTITY 命令的语法是什么？"

## 运行完整构建

1. 首次运行（从头开始）
python main.py

2. 断点续传（自动检测进度）
python main.py

3. 测试模式（只处理 1 个文件）
python main.py --limit 1

4. 指定目录 + 重置进度
python main.py --input ./my_md_files --reset

✅ 预期输出：
控制台：实时日志 + 进度
文件：afsim_dataset/afsim_sft_dataset.jsonl (最终数据)
文件：afsim_dataset/progress.json (断点进度)
文件：afsim_dataset/build.log (详细日志)
