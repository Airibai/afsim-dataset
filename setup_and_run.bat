@echo off
echo ==========================================
echo MinerU PDF 批量转换 - 一键启动脚本
echo ==========================================

REM 1. 激活环境
echo 正在激活 conda 环境...
call conda activate mineru

if errorlevel 1 (
    echo 环境不存在，正在创建...
    call conda create -n mineru python=3.10 -y
    call conda activate mineru
    pip install magic-pdf[full] -i https://pypi.tuna.tsinghua.edu.cn/simple
)

REM 2. 创建目录
if not exist pdf_files mkdir pdf_files
if not exist markdown_files mkdir markdown_files

REM 3. 运行转换
echo 开始转换...
python batch_pdf_to_md_conda.py

echo 完成！
pause