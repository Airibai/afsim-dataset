# 🧪 `test_chunk.py` 完整使用流程

这是 AFSIM 数据集构建器的**分块测试工具**，用于验证 MD 文档分块效果。

---

## 📋 一、前置准备

### 1. 环境准备

```bash
# 1.1 创建虚拟环境（可选但推荐）
python -m venv afsim_env
source afsim_env/bin/activate  # Linux/Mac
# 或
afsim_env\Scripts\activate     # Windows

# 1.2 安装依赖
pip install -r requirements.txt

# 1.3 验证安装
python -c "import requests; print('✅ requests 已安装')"
```

### 2. 配置 API Key（可选）

虽然分块测试**不需要调用 API**，但建议配置好环境变量：

```bash
# Linux/Mac
export ZHIPU_API_KEY="sk-xxxxxxxxxxxxxxxx"

# Windows PowerShell
$env:ZHIPU_API_KEY="sk-xxxxxxxxxxxxxxxx"

# Windows CMD
set ZHIPU_API_KEY=sk-xxxxxxxxxxxxxxxx
```

### 3. 准备 MD 文件

确保 `./markdown_files/` 目录下有 MinerU 转换后的 MD 文件：

```bash
# 检查文件
ls -lh ./markdown_files/*.md

# 如果没有，先运行 MinerU 转换
# 参考之前的 batch_convert_cli.py 脚本
```

---

## 🚀 二、使用场景

### 场景 1：测试单个文件分块（最常用）

```bash
# 语法
python test_chunk.py --file <路径到 MD 文件>

# 示例
python test_chunk.py --file ./markdown_files/AFSIM2.9 参考手册-v1.1_1-40.md
```

**预期输出**：
```
🧪 测试分块：AFSIM2.9 参考手册-v1.1_1-40.md
📊 配置：min=2000, max=5000 tokens

📄 分块处理：AFSIM2.9 参考手册-v1.1_1-40.md
✅ 分块完成：AFSIM2.9 参考手册-v1.1_1-40.md → 8 块

✅ 成功分块：8 块
📈 Token 分布：min=2100, max=4800, avg=3200

======================================================================
📦 块 #1/8
📄 文件：AFSIM2.9 参考手册-v1.1_1-40.md
📍 位置：字符 [0:8500]
🔢 Token 估算：3200
----------------------------------------------------------------------
📝 内容预览：
# 第 1 章 AFSIM 概述

## 1.1 系统介绍
AFSIM (Advanced Framework for Simulation...)

...(省略)

======================================================================

💾 分块元数据已保存：./afsim_dataset/test/AFSIM2.9 参考手册-v1.1_1-40_chunks.json
💡 提示：完整内容可在代码中通过 chunk.content 访问

✅ 测试完成！
```

---

### 场景 2：测试目录下多个文件

```bash
# 语法
python test_chunk.py --dir <目录路径> --limit <文件数量>

# 示例：测试前 3 个文件
python test_chunk.py --dir ./markdown_files --limit 3

# 示例：测试全部文件
python test_chunk.py --dir ./markdown_files
```

**预期输出**：
```
📁 扫描目录：./markdown_files，找到 63 个 MD 文件
📋 限制处理前 3 个文件

📄 分块处理：AFSIM2.9 参考手册-v1.1_1-40.md
✅ 分块完成：AFSIM2.9 参考手册-v1.1_1-40.md → 8 块

======================================================================
📦 块 #1/8
📄 文件：AFSIM2.9 参考手册-v1.1_1-40.md
...

📄 分块处理：AFSIM2.9 参考手册-v1.1_41-80.md
✅ 分块完成：AFSIM2.9 参考手册-v1.1_41-80.md → 7 块

📄 分块处理：AFSIM2.9 参考手册-v1.1_81-120.md
✅ 分块完成：AFSIM2.9 参考手册-v1.1_81-120.md → 9 块

📊 批量测试完成：3 文件 → 24 块

✅ 测试完成！
```

---

### 场景 3：从环境变量重载配置

```bash
# 临时修改分块参数
export CHUNK_MIN_TOKENS=3000
export CHUNK_MAX_TOKENS=6000

# 使用 --env 参数重载
python test_chunk.py --file ./markdown_files/AFSIM2.9 参考手册-v1.1_1-40.md --env
```

**预期输出**：
```
🔄 已从环境变量重载配置
📊 配置：min=3000, max=6000 tokens
...
```

---

### 场景 4：查看帮助信息

```bash
python test_chunk.py --help
```

**预期输出**：
```
usage: test_chunk.py [-h] [-f FILE] [-d DIR] [-l LIMIT] [--env]

测试文档分块功能

选项:
  -h, --help            显示此帮助信息
  -f, --file FILE       测试单个 MD 文件
  -d, --dir DIR         测试目录（默认：./markdown_files）
  -l, --limit LIMIT     目录模式下限制文件数
  --env                 从环境变量重载配置
```

---

## 📊 三、输出文件说明

### 1. 控制台输出

| 信息 | 说明 |
|------|------|
| `📦 块 #X/Y` | 当前块序号/总块数 |
| `📍 位置：字符 [start:end]` | 原文本中的字符位置 |
| `🔢 Token 估算：XXX` | 该块的 Token 数量估算 |
| `📈 Token 分布` | 所有块的最小/最大/平均 Token 数 |

### 2. 生成的 JSON 文件

**位置**：`./afsim_dataset/test/<文件名>_chunks.json`

**内容结构**：
```json
[
  {
    "filename": "AFSIM2.9 参考手册-v1.1_1-40.md",
    "chunk_index": 0,
    "total_chunks": 8,
    "char_start": 0,
    "char_end": 8500,
    "token_estimate": 3200
  },
  {
    "filename": "AFSIM2.9 参考手册-v1.1_1-40.md",
    "chunk_index": 1,
    "total_chunks": 8,
    "char_start": 7650,
    "char_end": 16200,
    "token_estimate": 3100
  }
  // ... 更多块
]
```

**注意**：JSON 中**不包含完整内容**（避免文件过大），只包含元数据。完整内容需在代码中通过 `chunk.content` 访问。

---

## 🔍 四、验证分块质量

### 检查点 1：Token 分布是否合理

```bash
# 理想情况
min >= 2000  # 不低于最小值
max <= 5000  # 不超过最大值
avg ≈ 3500   # 平均值在中间

# 如果 min < 2000
# → 文件内容太少，或分块逻辑有问题

# 如果 max > 5000
# → 需要调整 CHUNK_MAX_TOKENS 参数
```

### 检查点 2：块边界是否在合理位置

```bash
# 查看生成的 JSON
cat ./afsim_dataset/test/AFSIM2.9 参考手册-v1.1_1-40_chunks.json | python -m json.tool

# 检查 char_start/char_end 是否有重叠
# 正常情况：后一块的 start 应 < 前一块的 end（有重叠）
```

### 检查点 3：内容预览是否完整

```bash
# 修改 test_chunk.py，增加预览长度
# 找到 visualize_chunk 函数，修改 max_preview 参数
max_preview: int = 500  # 从 300 改为 500
```

---

## ⚠️ 五、常见问题排查

### 问题 1：`ModuleNotFoundError: No module named 'requests'`

**原因**：依赖未安装

**解决**：
```bash
pip install -r requirements.txt
# 或
pip install requests
```

---

### 问题 2：`❌ 文件不存在：xxx.md`

**原因**：路径错误或文件不存在

**解决**：
```bash
# 检查文件是否存在
ls -lh ./markdown_files/*.md

# 使用绝对路径
python test_chunk.py --file /absolute/path/to/file.md

# 或切换到正确目录
cd /path/to/project
python test_chunk.py --file ./markdown_files/file.md
```

---

### 问题 3：`⚠️ 文件为空` 或 `⚠️ 无法分块`

**原因**：MD 文件内容为空或太少

**解决**：
```bash
# 检查文件内容
head -n 20 ./markdown_files/file.md

# 如果确实为空，重新运行 MinerU 转换
# 如果内容太少（<500 字符），跳过该文件
```

---

### 问题 4：分块数量异常（太多/太少）

**原因**：Token 估算参数不匹配实际内容

**解决**：
```bash
# 调整分块参数（环境变量方式）
export CHUNK_MIN_TOKENS=1500
export CHUNK_MAX_TOKENS=4000
python test_chunk.py --file xxx.md --env

# 或修改 config.py
# ChunkConfig 类中调整 min_tokens/max_tokens
```

---

### 问题 5：中文内容 Token 估算不准

**原因**：当前使用字符估算（±15% 误差）

**解决**：
```bash
# 方案 1：接受误差（有 10% 重叠缓冲，不影响使用）

# 方案 2：使用 tiktoken 精确计算（需安装）
pip install tiktoken

# 修改 token_utils.py，启用精确计算
# （需要确认 GLM 模型的 tokenizer）
```

---

## 📋 六、完整测试流程示例

```bash
# ==================== 步骤 1: 准备环境 ====================
python -m venv afsim_env
source afsim_env/bin/activate
pip install -r requirements.txt

# ==================== 步骤 2: 检查 MD 文件 ====================
ls -lh ./markdown_files/*.md | head -5

# ==================== 步骤 3: 测试单个文件 ====================
python test_chunk.py --file ./markdown_files/AFSIM2.9 参考手册-v1.1_1-40.md

# ==================== 步骤 4: 测试多个文件 ====================
python test_chunk.py --dir ./markdown_files --limit 5

# ==================== 步骤 5: 查看输出 ====================
ls -lh ./afsim_dataset/test/
cat ./afsim_dataset/test/AFSIM2.9 参考手册-v1.1_1-40_chunks.json | python -m json.tool | head -30

# ==================== 步骤 6: 查看日志 ====================
cat ./afsim_dataset/build.log | tail -50

# ==================== 步骤 7: 确认无误后运行主程序 ====================
python main.py --limit 1  # 先测试 1 个文件
```

---

## 🎯 七、参数调优建议

| 参数 | 默认值 | 调优场景 | 建议值 |
|------|--------|---------|--------|
| `min_tokens` | 2000 | 块太小，API 调用次数多 | 3000 |
| `max_tokens` | 5000 | 块太大，超出模型上下文 | 4000 |
| `overlap_ratio` | 0.1 | 块之间上下文不连贯 | 0.15 |

**修改方式**：
```bash
# 环境变量（临时）
export CHUNK_MIN_TOKENS=3000
export CHUNK_MAX_TOKENS=4000
export CHUNK_OVERLAP_RATIO=0.15

# 运行测试
python test_chunk.py --file xxx.md --env
```

---

## ✅ 八、测试通过标准

分块测试通过后，应满足以下条件：

- [ ] 所有 MD 文件都能正常分块
- [ ] Token 分布在 [2000, 5000] 区间内
- [ ] 块边界在段落/代码块边界（不切断语义）
- [ ] 生成的 JSON 元数据完整
- [ ] 日志无 ERROR 级别错误

**全部满足后，即可运行 `main.py` 进行完整数据集构建！** 🚀

---

有任何问题随时告诉我！😊