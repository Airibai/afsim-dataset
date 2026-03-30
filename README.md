# afsim-dataset
调用minerU将原始50个pdf解析成md

# 一、创建 Conda 环境
## 1. 创建独立环境（推荐 Python 3.10）
创建名为 mineru 的 conda 环境，Python 版本 3.10
conda create -n mineru python=3.10 -y

激活环境
conda activate mineru

验证环境
python --version
which python  # Linux/Mac
或 where python  # Windows

## 2.安装 MinerU 依赖
# 方式 1：pip 安装（推荐）
pip install magic-pdf[full] -i https://pypi.tuna.tsinghua.edu.cn/simple

# 方式 2：如果上面失败，分步安装
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install magic-pdf
pip install unimernet  # 公式识别
pip install paddlepaddle-gpu  # 可选，OCR 支持

## 3. 验证安装
# 检查 MinerU 版本
magic-pdf --version

# 测试导入
python -c "import magic_pdf; print('MinerU 导入成功')"

# Conda 环境管理命令
 查看所有环境
conda env list

 激活 mineru 环境
conda activate mineru

 查看已安装的包
conda list
 或
pip list

 更新 MinerU
pip install -U magic-pdf[full]

 导出环境配置（便于分享）
conda env export > mineru_environment.yml

 从配置文件创建环境
conda env create -f mineru_environment.yml

 删除环境
conda env remove -n mineru