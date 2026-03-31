# 🧪 `test_single_query.py` 完整使用流程

这是 AFSIM 数据集构建器的**单次问答测试工具**，用于验证 GLM API 调用、数据集生成、关键内容提取等功能。

---

## 📋 一、前置准备

### 1. 环境准备

```bash
# 1.1 激活虚拟环境
source afsim_env/bin/activate  # Linux/Mac
# 或
afsim_env\Scripts\activate     # Windows

# 1.2 确认依赖已安装
pip install -r requirements.txt

# 1.3 验证导入
python -c "from glm_client import GLMClient; print('✅ 模块导入成功')"
```

### 2. 配置 API Key（必需）

```bash
# Linux/Mac
export ZHIPU_API_KEY="sk-xxxxxxxxxxxxxxxx"

# Windows PowerShell
$env:ZHIPU_API_KEY="sk-xxxxxxxxxxxxxxxx"

# Windows CMD
set ZHIPU_API_KEY=sk-xxxxxxxxxxxxxxxx

# 验证配置
echo $ZHIPU_API_KEY  # Linux/Mac
echo $env:ZHIPU_API_KEY  # PowerShell
```

### 3. 测试 API 连通性

```bash
# 运行测试脚本会自动检测连接
python test_single_query.py
```

---

## 🚀 二、使用场景

### 场景 1：查看帮助信息（首次使用）

```bash
python test_single_query.py --help
```

**预期输出**：
```
usage: test_single_query.py [-h] [-i] [-c CONTENT] [-f FILE]
                            [--test-summary] [--env]

测试单次问答功能

选项:
  -h, --help            显示此帮助信息
  -i, --interactive     交互式测试模式
  -c, --content CONTENT
                        测试内容字符串
  -f, --file FILE       从文件读取测试内容
  --test-summary        仅测试关键内容提取
  --env                 从环境变量重载配置
```

---

### 场景 2：自动 API 连接测试（默认）

```bash
python test_single_query.py
```

**预期输出**：
```
🔌 测试 API 连接...
✅ 连接成功！
🤖 回复：你好！我是智谱清言，基于 GLM 大模型训练的 AI 助手...
📊 用量：{'prompt_tokens': 15, 'completion_tokens': 48, 'total_tokens': 63}

📋 可用命令:
  -i, --interactive     交互式测试模式
  -c, --content CONTENT
                        测试内容字符串
  -f, --file FILE       从文件读取测试内容
  --test-summary        仅测试关键内容提取
  --env                 从环境变量重载配置

✅ 测试完成！
```

**如果失败**：
```
❌ 连接失败：401 Unauthorized: API Key 无效或过期
❌ API 连接失败，请检查配置后重试
```

---

### 场景 3：交互式测试模式（推荐）

```bash
python test_single_query.py --interactive
```

**预期输出**：
```
🔌 测试 API 连接...
✅ 连接成功！

🎮 进入交互式测试模式
💡 输入内容后按回车，输入 /exit 退出

📝 输入手册内容片段 (或 /exit): ENTITY 命令用于定义仿真实体，语法如下：
ENTITY <name> TYPE <type> {
    MODEL "<model_name>"
    POSITION <lat> <lon> <alt>
}

🔌 测试 API 连接...
✅ 连接成功！
📡 发送请求...
🤖 助手：[{"instruction": "请解释 AFSIM 中 ENTITY 命令的作用", "input": "", "output": "ENTITY 命令用于定义仿真实体..."}]

✅ 生成 3 条数据
📋 示例：请解释 AFSIM 中 ENTITY 命令的作用...
📊 历史窗口：1 条

📝 输入手册内容片段 (或 /exit): /exit
```

---

### 场景 4：指定内容字符串测试

```bash
python test_single_query.py \
  --content "ENTITY 命令用于定义仿真实体，语法如下：ENTITY <name> TYPE <type> { MODEL \"F-16\" POSITION 35.0 110.0 5000 }"
```

**预期输出**：
```
🔌 测试 API 连接...
✅ 连接成功！

🧪 测试单次查询
📄 模拟文件：manual_input
📝 内容长度：120 字符

📡 发送请求...
🤖 助手：[{"instruction": "请解释 AFSIM 中 ENTITY 命令的语法", "output": "ENTITY 命令用于定义仿真实体..."}]

🔍 解析响应...
✅ 解析出 3 条有效数据

【数据#1】
问：请解释 AFSIM 中 ENTITY 命令的语法
答：ENTITY 命令用于定义仿真实体，基本语法为：ENTITY <name> TYPE <type> {...}...

【数据#2】
问：如何在 AFSIM 中部署一架 F-16 战斗机？
答：使用 ENTITY 命令部署 F-16 的示例如下：ENTITY F16_01 TYPE Aircraft { MODEL "F-16" POSITION 35.0 110.0 5000 }...

🔍 测试关键内容提取...
📋 提取结果：
  提问要点：AFSIM 实体定义语法
  知识点：ENTITY 命令的格式、参数含义、使用示例
  数据总结：生成 3 条 Alpaca 格式训练数据

💾 测试输出已保存：./afsim_dataset/test/single_query_test.json

✅ 测试完成！
```

---

### 场景 5：从 MD 文件读取内容测试

```bash
python test_single_query.py \
  --file ./markdown_files/AFSIM2.9 参考手册-v1.1_1-40.md
```

**预期输出**：
```
🔌 测试 API 连接...
✅ 连接成功！

🧪 测试单次查询
📄 模拟文件：AFSIM2.9 参考手册-v1.1_1-40.md
📝 内容长度：45000 字符

📡 发送请求...
🤖 助手：[流式输出中...]

🔍 解析响应...
✅ 解析出 12 条有效数据

【数据#1】
问：AFSIM 系统的主要功能是什么？
答：AFSIM (Advanced Framework for Simulation, Integration and Modeling) 是一个...

【数据#2】
问：如何在 AFSIM 中定义飞行器实体？
答：使用 ENTITY 命令定义飞行器，语法如下：ENTITY <name> TYPE Aircraft {...}...

...（更多数据）

🔍 测试关键内容提取...
📋 提取结果：
  提问要点：AFSIM 系统概述与实体定义
  知识点：系统架构、实体命令、参数说明、代码示例
  数据总结：生成 12 条 Alpaca 格式训练数据，覆盖核心概念

💾 测试输出已保存：./afsim_dataset/test/single_query_test.json

✅ 测试完成！
```

---

### 场景 6：仅测试关键内容提取功能

```bash
python test_single_query.py --test-summary
```

**预期输出**：
```
🔌 测试 API 连接...
✅ 连接成功！

🧪 测试关键内容提取
📝 模拟输入：2 条数据
✅ 提取结果：
  key_summary: AFSIM 实体定义语法与参数说明
  question_summary: AFSIM 手册内容问答
  dataset_summary: 生成 2 条训练样本

✅ 测试完成！
```

---

### 场景 7：从环境变量重载配置

```bash
# 临时修改模型
export ZHIPU_MODEL="glm-4-plus"

# 运行测试
python test_single_query.py --content "测试内容" --env
```

**预期输出**：
```
🔄 已从环境变量重载配置
🔌 测试 API 连接...
✅ 连接成功！
...
```

---

## 📊 三、输出文件说明

### 1. 测试输出 JSON

**位置**：`./afsim_dataset/test/single_query_test.json`

**内容结构**：
```json
{
  "timestamp": "2026-03-30T16:30:00.123456",
  "filename": "AFSIM2.9 参考手册-v1.1_1-40.md",
  "content_preview": "ENTITY 命令用于定义仿真实体...",
  "response_preview": "[{\"instruction\": \"请解释...\", \"output\": \"ENTITY 命令...\"}]",
  "datasets_count": 12,
  "datasets_sample": [
    {
      "instruction": "请解释 AFSIM 中 ENTITY 命令的语法",
      "input": "",
      "output": "ENTITY 命令用于定义仿真实体..."
    }
  ],
  "key_contents": {
    "question_summary": "AFSIM 实体定义语法",
    "key_summary": "ENTITY 命令的格式、参数含义、使用示例",
    "dataset_summary": "生成 12 条 Alpaca 格式训练数据"
  }
}
```

**用途**：
- 调试 API 响应质量
- 验证数据集格式
- 检查关键内容提取效果

---

### 2. 控制台输出

| 标识 | 含义 |
|------|------|
| `🔌` | API 连接测试 |
| `🧪` | 测试类型说明 |
| `📡` | 发送请求 |
| `🤖` | 模型流式输出 |
| `🔍` | 解析/提取操作 |
| `✅` | 成功 |
| `❌` | 失败 |
| `💾` | 文件保存 |

---

## 🔍 四、验证测试质量

### 检查点 1：API 连接是否正常

```bash
# 成功标志
✅ 连接成功！
📊 用量：{'prompt_tokens': XX, 'completion_tokens': XX, 'total_tokens': XX}

# 失败标志
❌ 连接失败：401 Unauthorized
❌ 连接失败：ConnectionError
```

---

### 检查点 2：数据集解析是否成功

```bash
# 成功标志
✅ 解析出 X 条有效数据

# 失败标志
⚠️  数据集解析失败，响应前 200 字符：...
✅ 解析出 0 条有效数据  # 模型输出格式不对
```

**如果解析失败**：
1. 查看 `single_query_test.json` 中的 `response_preview`
2. 检查模型是否输出了正确的 JSON 格式
3. 调整 `config.py` 中的 `system_prompt`，强调 JSON 输出

---

### 检查点 3：关键内容提取是否合理

```bash
# 检查提取结果
📋 提取结果：
  提问要点：XX  # 应≤100 字，概括核心问题
  知识点：XX    # 应≤500 字，总结关键知识
  数据总结：XX  # 应≤100 字，说明数据情况
```

---

### 检查点 4：生成的数据格式是否正确

```bash
# 查看测试输出
cat ./afsim_dataset/test/single_query_test.json | python -m json.tool

# 检查字段
{
  "instruction": "问题/指令",  # 必需
  "input": "可选上下文",       # 可选
  "output": "详细回答"         # 必需，应≥50 字
}
```

---

## ⚠️ 五、常见问题排查

### 问题 1：`ZHIPU_API_KEY 未配置`

**原因**：环境变量未设置

**解决**：
```bash
# Linux/Mac
export ZHIPU_API_KEY="sk-xxxxxx"

# Windows PowerShell
$env:ZHIPU_API_KEY="sk-xxxxxx"

# 验证
echo $ZHIPU_API_KEY

# 重新运行
python test_single_query.py
```

---

### 问题 2：`401 Unauthorized: API Key 无效`

**原因**：Key 错误/过期/权限不足

**解决**：
```bash
# 1. 重新获取 Key
# 访问 https://open.bigmodel.cn → 控制台 → API 管理 → 创建新 Key

# 2. 更新环境变量
export ZHIPU_API_KEY="sk-新 Key"

# 3. 验证权限
# 确认账户已开通 GLM-4-Flash 模型权限
```

---

### 问题 3：`429 Too Many Requests`

**原因**：请求频率超限

**解决**：
```bash
# 方案 1：等待片刻后重试
sleep 60
python test_single_query.py

# 方案 2：修改 config.py 增加重试延迟
# APIConfig 类中
retry_delay: float = 5.0  # 从 2.0 改为 5.0
```

---

### 问题 4：`数据集解析失败`

**原因**：模型输出不是纯 JSON，包含额外文字

**解决**：
```bash
# 方案 1：查看原始响应
cat ./afsim_dataset/test/single_query_test.json | python -m json.tool

# 方案 2：调整 system_prompt，强调只输出 JSON
# config.py 中
system_prompt = """...
**禁止行为：**
- 不要输出"好的"、"以下是"等引导语
- 不要添加```json```标记
..."""

# 方案 3：修改解析逻辑（conversation.py）
# parse_dataset_response 函数已支持多种格式提取
```

---

### 问题 5：`生成数据数量为 0`

**原因**：内容太少/模型拒绝生成/解析失败

**解决**：
```bash
# 方案 1：增加内容长度（至少 500 字符）
python test_single_query.py --file ./markdown_files/xxx.md

# 方案 2：检查 API 响应
# 查看 single_query_test.json 中的 response_preview

# 方案 3：调整 temperature 参数
# config.py 中
temperature: float = 0.8  # 从 0.7 改为 0.8，增加创造性
```

---

### 问题 6：`请求超时`

**原因**：网络问题/内容太长

**解决**：
```bash
# 方案 1：增加超时时间
# config.py 中
timeout: int = 180  # 从 120 改为 180

# 方案 2：检查网络
ping open.bigmodel.cn

# 方案 3：减少内容长度
# 测试时用小文件
python test_single_query.py --file ./markdown_files/小文件.md
```

---

## 📋 六、完整测试流程示例

```bash
# ==================== 步骤 1: 准备环境 ====================
source afsim_env/bin/activate
pip install -r requirements.txt

# ==================== 步骤 2: 配置 API Key ====================
export ZHIPU_API_KEY="sk-xxxxxxxxxxxxxxxx"
echo $ZHIPU_API_KEY  # 验证

# ==================== 步骤 3: 测试 API 连接 ====================
python test_single_query.py

# ==================== 步骤 4: 交互式测试 ====================
python test_single_query.py --interactive
# 输入一些 AFSIM 手册内容，观察输出

# ==================== 步骤 5: 文件测试 ====================
python test_single_query.py --file ./markdown_files/AFSIM2.9 参考手册-v1.1_1-40.md

# ==================== 步骤 6: 查看输出 ====================
cat ./afsim_dataset/test/single_query_test.json | python -m json.tool | head -50

# ==================== 步骤 7: 验证数据格式 ====================
python -c "
import json
with open('./afsim_dataset/test/single_query_test.json') as f:
    data = json.load(f)
    print(f'生成数据：{data[\"datasets_count\"]} 条')
    print(f'示例问题：{data[\"datasets_sample\"][0][\"instruction\"][:50]}...')
"

# ==================== 步骤 8: 确认无误后运行主程序 ====================
python main.py --limit 1
```

---

## 🎯 七、参数调优建议

| 参数 | 默认值 | 调优场景 | 建议值 |
|------|--------|---------|--------|
| `temperature` | 0.7 | 数据太单一 | 0.8-0.9 |
| `temperature` | 0.7 | 数据太随机 | 0.3-0.5 |
| `max_tokens` | 4096 | 输出被截断 | 6144 |
| `timeout` | 120 | 经常超时 | 180-300 |
| `max_retries` | 3 | 网络不稳定 | 5 |

**修改方式**：
```bash
# 环境变量（临时）
export ZHIPU_TEMPERATURE=0.8
export ZHIPU_MAX_TOKENS=6144

# 或修改 config.py
# APIConfig 类中调整对应参数
```

---

## ✅ 八、测试通过标准

单次问答测试通过后，应满足以下条件：

- [ ] API 连接成功，无 401/429 错误
- [ ] 能正常接收流式响应
- [ ] 数据集解析成功（≥1 条有效数据）
- [ ] 数据格式符合 Alpaca 规范（instruction + output）
- [ ] 关键内容提取成功（3 个总结字段都有值）
- [ ] 测试 JSON 文件正常生成
- [ ] 日志无 ERROR 级别错误

**全部满足后，即可运行 `main.py` 进行完整数据集构建！** 🚀

---

## 📊 九、与 test_chunk.py 的对比

| 特性 | test_chunk.py | test_single_query.py |
|------|---------------|---------------------|
| **用途** | 测试文档分块 | 测试 API 问答 |
| **需要 API Key** | ❌ 不需要 | ✅ 必需 |
| **产生费用** | ❌ 无 | ✅ 有（少量） |
| **输出文件** | `*_chunks.json` | `single_query_test.json` |
| **测试内容** | 本地文件处理 | 网络 API 调用 |
| **运行顺序** | 先运行 | 后运行 |

**推荐测试顺序**：
```bash
# 1. 先测试分块（无成本）
python test_chunk.py --file xxx.md

# 2. 再测试问答（验证 API）
python test_single_query.py --file xxx.md

# 3. 最后运行主程序
python main.py
```

---

有任何问题随时告诉我！😊