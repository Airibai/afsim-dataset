#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinerU API 批量 PDF 转 Markdown 转换器
使用 Precision Parsing API (v4) - 支持本地文件上传
适配 63 个 × 50 页 AFSIM 手册场景
"""

import os
import sys
import time
import json
import shutil
import zipfile
import logging
import requests
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==================== 配置区域 ====================
CONFIG = {
    # 🔑 必填：从 https://mineru.net 获取
    "token": "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI4MDkwMDY5MiIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc3NDg1NTIwMywiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiIiwib3BlbklkIjpudWxsLCJ1dWlkIjoiMmJkZjBkYzEtOGJlYi00ZjYwLWFmMWMtZWZkOWEyMTcwMTg1IiwiZW1haWwiOiIiLCJleHAiOjE3ODI2MzEyMDN9.sd9mG8LYCpS9FKqOJswjrP5eDPkkTCy5OJfEY1R98BIMO6zhOuzJPGnHIO7dZJMvRcn50ZucLzWIC7VeJPVSGw",
    
    # 📁 路径配置
    "input_dir": "./pdf_files",           # 本地 PDF 输入目录
    "output_dir": "./markdown_files",      # Markdown 输出目录
    "temp_dir": "./upload_temp",           # 临时上传目录（自动清理）
    
    # ⚙️ 解析参数
    "model_version": "vlm",               # 推荐: vlm(高精度) / pipeline(快速)
    "language": "ch",                      # 文档语言: ch=中文, en=英文
    "enable_ocr": False,                   # 是否启用 OCR（文字版 PDF 可关闭加速）
    "enable_table": True,                  # 启用表格识别
    "enable_formula": True,                # 启用公式识别
    
    # ⏱️ 轮询配置
    "poll_interval": 10,                   # 轮询间隔(秒)
    "poll_timeout": 3600,                  # 单任务超时(秒)
    "batch_size": 50,                      # 每批提交文件数（≤200）
    
    # 🔄 重试配置
    "max_retries": 3,                      # 网络错误重试次数
    "retry_delay": 5,                      # 重试间隔(秒)
}
# ================================================

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('api_conversion.log', encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

class MinerUAPIClient:
    """MinerU Precision API 客户端"""
    
    BASE_URL = "https://mineru.net/api/v4"
    
    def __init__(self, token: str):
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        })
    
    def _request(self, method: str, endpoint: str, **kwargs) -> dict:
        """带重试的请求封装"""
        url = f"{self.BASE_URL}{endpoint}"
        for attempt in range(CONFIG["max_retries"]):
            try:
                resp = self.session.request(method, url, timeout=60, **kwargs)
                resp.raise_for_status()
                result = resp.json()
                if result.get("code") != 0:
                    raise Exception(f"API 错误: {result.get('msg')}")
                return result
            except requests.exceptions.RequestException as e:
                if attempt == CONFIG["max_retries"] - 1:
                    raise
                logger.warning(f"请求失败，{CONFIG['retry_delay']}s 后重试: {e}")
                time.sleep(CONFIG["retry_delay"])
    
    def get_upload_urls(self, files: list[dict]) -> dict:
        """
        批量获取文件上传 URL
        files: [{"name": "xxx.pdf", "data_id": "optional_id"}, ...]
        """
        payload = {
            "files": files,
            "model_version": CONFIG["model_version"],
            "language": CONFIG["language"],
            "enable_ocr": CONFIG["enable_ocr"],
            "enable_table": CONFIG["enable_table"],
            "enable_formula": CONFIG["enable_formula"],
        }
        result = self._request("POST", "/file-urls/batch", json=payload)
        return result["data"]  # {batch_id, file_urls}
    
    def upload_file(self, file_url: str, file_path: str) -> bool:
        """上传单个文件到 OSS（PUT 方法，无需认证头）"""
        try:
            with open(file_path, "rb") as f:
                resp = requests.put(file_url, data=f, timeout=300)
                return resp.status_code in (200, 201)
        except Exception as e:
            logger.error(f"上传失败 {file_path}: {e}")
            return False
    
    def poll_batch_result(self, batch_id: str) -> list[dict]:
        """轮询批量任务结果，返回完成的任务列表"""
        start_time = time.time()
        
        while time.time() - start_time < CONFIG["poll_timeout"]:
            result = self._request("GET", f"/extract-results/batch/{batch_id}")
            extract_results = result["data"].get("extract_result", [])
            
            # 收集已完成或失败的任务
            finished = [r for r in extract_results if r["state"] in ("done", "failed")]
            running = [r for r in extract_results if r["state"] not in ("done", "failed")]
            
            if finished:
                logger.info(f"批次进度: {len(finished)} 完成, {len(running)} 进行中")
            
            if not running:  # 全部完成
                return extract_results
            
            time.sleep(CONFIG["poll_interval"])
        
        raise TimeoutError(f"轮询超时 ({CONFIG['poll_timeout']}s)")
    
    def download_and_extract_md(self, zip_url: str, output_path: Path) -> bool:
        """下载 ZIP 并提取 full.md 到指定路径"""
        try:
            # 下载 ZIP
            resp = requests.get(zip_url, stream=True, timeout=300)
            resp.raise_for_status()
            
            # 保存到临时文件
            temp_zip = output_path.parent / f"{output_path.stem}.zip"
            with open(temp_zip, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # 解压并提取 full.md
            with zipfile.ZipFile(temp_zip, "r") as zf:
                # MinerU 输出结构: {name}/auto/{name}.md 或 full.md
                md_names = [n for n in zf.namelist() if n.endswith("full.md") or n.endswith(".md")]
                if not md_names:
                    raise Exception("ZIP 中未找到 Markdown 文件")
                
                # 提取第一个匹配的 .md 文件
                target_md = md_names[0]
                zf.extract(target_md, output_path.parent)
                
                # 移动并重命名
                extracted = output_path.parent / target_md
                if extracted != output_path:
                    shutil.move(str(extracted), str(output_path))
            
            # 清理临时 ZIP
            temp_zip.unlink(missing_ok=True)
            return True
            
        except Exception as e:
            logger.error(f"下载/解压失败: {e}")
            return False


def batch_convert_api():
    """主转换流程"""
    token = CONFIG["token"]
    if token == "your_token_here":
        logger.error("❌ 请配置 CONFIG['token'] 为您的 MinerU API Token")
        logger.info("获取方式: 登录 https://mineru.net → 个人中心 → API 管理")
        return
    
    input_dir = Path(CONFIG["input_dir"])
    output_dir = Path(CONFIG["output_dir"])
    temp_dir = Path(CONFIG["temp_dir"])
    
    # 创建目录
    output_dir.mkdir(parents=True, exist_ok=True)
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # 收集 PDF 文件
    pdf_files = list(input_dir.glob("*.pdf")) + list(input_dir.glob("*.PDF"))
    pdf_files = list(set(pdf_files))
    
    if not pdf_files:
        logger.error(f"❌ 在 {input_dir} 中未找到 PDF 文件")
        return
    
    total_pages = len(pdf_files) * 50  # 估算
    logger.info("=" * 60)
    logger.info(f"MinerU API 批量转换启动")
    logger.info(f"文件数: {len(pdf_files)} | 估算页数: {total_pages}")
    logger.info(f"免费配额: 2000 页/天 | 预计需 {total_pages/2000:.1f} 天")
    logger.info(f"模型: {CONFIG['model_version']} | 语言: {CONFIG['language']}")
    logger.info("=" * 60)
    
    # 初始化客户端
    client = MinerUAPIClient(token)
    
    stats = {"success": 0, "failed": 0, "skipped": 0}
    failed_details = []
    
    # 分批处理（每批 ≤200 文件）
    for batch_idx in range(0, len(pdf_files), CONFIG["batch_size"]):
        batch_files = pdf_files[batch_idx:batch_idx + CONFIG["batch_size"]]
        batch_num = batch_idx // CONFIG["batch_size"] + 1
        total_batches = (len(pdf_files) + CONFIG["batch_size"] - 1) // CONFIG["batch_size"]
        
        logger.info(f"\n📦 处理批次 {batch_num}/{total_batches} ({len(batch_files)} 个文件)")
        
        # 1. 准备文件列表（跳过已转换的）
        file_list = []
        for pdf in batch_files:
            md_path = output_dir / f"{pdf.stem}.md"
            if CONFIG.get("skip_existing", True) and md_path.exists():
                logger.info(f"⊘ 跳过 (已存在): {pdf.name}")
                stats["skipped"] += 1
                continue
            file_list.append({"name": pdf.name})
        
        if not file_list:
            continue
        
        # 2. 获取上传 URL
        try:
            upload_data = client.get_upload_urls(file_list)
            batch_id = upload_data["batch_id"]
            file_urls = upload_data["file_urls"]  # 顺序与 file_list 一致
            logger.info(f"✓ 获取上传链接, batch_id: {batch_id}")
        except Exception as e:
            logger.error(f"✗ 获取上传链接失败: {e}")
            for f in file_list:
                stats["failed"] += 1
                failed_details.append({"file": f["name"], "error": str(e)})
            continue
        
        # 3. 上传文件到 OSS
        logger.info(f"📤 开始上传 {len(file_urls)} 个文件...")
        upload_success = []
        
        for idx, (file_info, upload_url) in enumerate(zip(file_list, file_urls)):
            pdf_path = input_dir / file_info["name"]
            if client.upload_file(upload_url, str(pdf_path)):
                upload_success.append(file_info)
                logger.debug(f"✓ 上传: {file_info['name']}")
            else:
                stats["failed"] += 1
                failed_details.append({"file": file_info["name"], "error": "上传失败"})
        
        if not upload_success:
            logger.error("✗ 本批次无文件上传成功，跳过")
            continue
        
        logger.info(f"✓ 上传完成 {len(upload_success)}/{len(file_urls)}")
        
        # 4. 轮询解析结果
        logger.info(f"⏳ 等待解析完成 (每 {CONFIG['poll_interval']}s 轮询)...")
        try:
            results = client.poll_batch_result(batch_id)
        except TimeoutError as e:
            logger.error(f"✗ 轮询超时: {e}")
            for f in upload_success:
                stats["failed"] += 1
                failed_details.append({"file": f["name"], "error": "轮询超时"})
            continue
        
        # 5. 下载并提取 Markdown
        logger.info(f"📥 下载解析结果...")
        for result in results:
            file_name = result["file_name"]
            state = result["state"]
            md_path = output_dir / f"{Path(file_name).stem}.md"
            
            if state == "done":
                zip_url = result.get("full_zip_url")
                if zip_url and client.download_and_extract_md(zip_url, md_path):
                    logger.info(f"✓ 完成: {file_name}")
                    stats["success"] += 1
                else:
                    logger.error(f"✗ 下载失败: {file_name}")
                    stats["failed"] += 1
                    failed_details.append({"file": file_name, "error": "下载/解压失败"})
            
            elif state == "failed":
                err_msg = result.get("err_msg", "未知错误")
                logger.error(f"✗ 解析失败: {file_name} - {err_msg}")
                stats["failed"] += 1
                failed_details.append({"file": file_name, "error": err_msg})
            
            else:
                logger.warning(f"⚠️  未知状态: {file_name} - {state}")
                stats["failed"] += 1
                failed_details.append({"file": file_name, "error": f"状态: {state}"})
        
        # 6. 配额检查提示
        if stats["success"] + stats["failed"] >= 40:  # 40×50=2000页
            logger.warning("⚠️  接近每日 2000 页配额，剩余文件建议明天继续")
    
    # 清理临时目录
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    
    # 输出报告
    logger.info("\n" + "=" * 60)
    logger.info("转换完成报告")
    logger.info("=" * 60)
    logger.info(f"成功: {stats['success']} | 失败: {stats['failed']} | 跳过: {stats['skipped']}")
    
    if failed_details:
        logger.warning("\n失败详情:")
        for item in failed_details[:10]:  # 只显示前 10 个
            logger.warning(f"  - {item['file']}: {item['error']}")
        if len(failed_details) > 10:
            logger.warning(f"  ... 还有 {len(failed_details)-10} 个")
    
    # 保存报告
    report_path = output_dir / "api_conversion_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "config": {k: v for k, v in CONFIG.items() if k != "token"},
            "stats": stats,
            "failed_details": failed_details
        }, f, ensure_ascii=False, indent=2)
    
    logger.info(f"\n报告已保存: {report_path}")
    logger.info("✅ 所有任务完成！")


if __name__ == "__main__":
    batch_convert_api()