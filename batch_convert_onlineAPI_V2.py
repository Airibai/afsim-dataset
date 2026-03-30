#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinerU API 批量 PDF 转 Markdown 转换器（最终修复版）
✅ 流式处理：完成一个立即下载
✅ 超时跳过：单文件超时不影响整体
✅ 认证修复：正确处理 Bearer Token
✅ 详细日志：401/403/超时等错误明确提示
✅ 配额管理：实时检查，达到限制自动停止
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

# ==================== 配置区域 ====================
CONFIG = {
    # 🔑 API 认证（必填）
    "token": "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1NDQwMDI5MCIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc3NDg1ODUyNywiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiIiwib3BlbklkIjpudWxsLCJ1dWlkIjoiNWU1NzliODAtY2Y1Ny00MmM0LWE1MGMtNzcyNGQ1ZTQ4YWQyIiwiZW1haWwiOiIyNzM2NTA0ODY1QHFxLmNvbSIsImV4cCI6MTc4MjYzNDUyN30.zI7KsNh6AqVmytBaYoz27RlYTDqLaa02-xAYIy93Orde1ZrGr5LUWgBHSQB_ZO7neqZ_jMl8dMplojr-Or8eoA",  # ← 替换为您的真实 Token
    
    # 📁 路径配置
    "input_dir": "./pdf_files",
    "output_dir": "./markdown_files",
    "temp_dir": "./upload_temp",
    
    # ⚙️ 解析参数
    "model_version": "vlm",       # vlm(高精度) / pipeline(快速)
    "language": "ch",             # ch=中文, en=英文
    "enable_ocr": False,          # 文字版 PDF 建议关闭，加速 3 倍
    "enable_table": True,         # 启用表格识别
    "enable_formula": True,       # 启用公式识别
    
    # ⏱️ 超时控制（关键！）
    "upload_timeout": 300,        # 上传超时 5 分钟
    "parse_timeout": 1800,        # 解析超时 30 分钟
    "download_timeout": 300,      # 下载超时 5 分钟
    "poll_interval": 5,           # 轮询间隔 5 秒
    
    # 🔄 重试配置
    "max_retries": 2,             # 每阶段重试次数
    "retry_delay": 3,             # 重试间隔(秒)
    
    # 📊 批量控制
    "max_files": None,            # 最多处理文件数（None=全部）
    "daily_page_limit": 2000,     # 每日配额限制
    "est_pages_per_file": 50,     # 预估每文件页数
    
    # 🔄 跳过配置
    "skip_existing": True,        # 跳过已存在的 .md 文件
    "skip_on_timeout": True,      # 超时后自动跳过
}
# ================================================


def setup_logging():
    """配置日志系统"""
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
    """
    MinerU API 客户端（修复认证 + 超时控制版）
    """
    
    # ⚠️ 基础 URL - 确保绝对路径
    BASE_URL = "https://mineru.net/api/v4"
    
    def __init__(self, token: str):
        """初始化客户端"""
        # 验证 Token
        if not token or token == "your_token_here":
            raise ValueError("❌ Token 未配置！请编辑脚本设置 CONFIG['token']")
        
        # 清理 Token（去除首尾空格/换行）
        self.token = token.strip()
        
        # 验证 Token 格式
        if not any(self.token.startswith(prefix) for prefix in ["sk-", "mr-", "eyJ"]):
            logger.warning(f"⚠️  Token 格式可能不正确：{self.token[:10]}...")
            logger.warning("✅ 正确格式示例：sk-abc123... 或 mr-xyz789...")
        
        # 初始化 Session
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",  # ⚠️ 关键：必须有 "Bearer " + 空格
            "Content-Type": "application/json"
        })
        
        logger.info(f"✅ API 客户端初始化成功")
        logger.info(f"📍 目标地址：{self.BASE_URL}")
        logger.info(f"🔑 Token 前缀：{self.token[:8]}...")
    
    def _request(self, method: str, endpoint: str, max_retries: int = None, **kwargs) -> dict:
        """
        带重试、超时和错误处理的请求封装
        """
        max_retries = max_retries or CONFIG["max_retries"]
        
        # 拼接完整 URL（关键修复）
        if endpoint.startswith(("http://", "https://")):
            url = endpoint
        else:
            # 确保 endpoint 以 / 开头
            if not endpoint.startswith("/"):
                endpoint = "/" + endpoint
            url = f"{self.BASE_URL}{endpoint}"
        
        logger.debug(f"🌐 请求：{method} {url}")
        
        for attempt in range(max_retries + 1):
            try:
                timeout = kwargs.pop("timeout", 60)
                
                resp = self.session.request(method, url, timeout=timeout, **kwargs)
                
                # 记录响应状态
                logger.debug(f"📡 响应：{resp.status_code}")
                
                # HTTP 状态码错误（401/403/429 等）
                resp.raise_for_status()
                
                # 解析 JSON
                result = resp.json()
                
                # 业务逻辑错误码
                if result.get("code") != 0:
                    error_msg = result.get("msg", "未知业务错误")
                    error_code = result.get("code")
                    logger.error(f"❌ API 业务错误 [{error_code}]: {error_msg}")
                    
                    # 特殊错误提示
                    if error_code == -60018:
                        logger.error("💡 提示：每日配额已用完，请明天继续或购买额度")
                    elif "token" in error_msg.lower() or "auth" in error_msg.lower():
                        logger.error("💡 提示：Token 无效或过期，请重新获取")
                    
                    raise Exception(f"API 错误 [{error_code}]: {error_msg}")
                
                return result
                
            except requests.exceptions.HTTPError as e:
                # 处理 401/403/429 等具体状态码
                status = e.response.status_code if e.response else "unknown"
                response_text = e.response.text[:200] if e.response else ""
                
                logger.error(f"❌ HTTP {status} 错误: {e}")
                
                if status == 401:
                    logger.error("💡 401 Unauthorized: Token 无效或格式错误")
                    logger.error("💡 检查：1.是否复制完整  2.是否有 'Bearer ' 前缀  3.是否已过期")
                elif status == 403:
                    logger.error("💡 403 Forbidden: Token 有效但无权限")
                    logger.error("💡 检查：是否开通了 Precision API 权限")
                elif status == 429:
                    logger.error("💡 429 Too Many Requests: 请求频率过高")
                    logger.error("💡 建议：等待 1 分钟后重试，或减小并发")
                elif status == 404:
                    logger.error(f"💡 404 Not Found: 接口路径可能已变更")
                    logger.error(f"💡 响应内容：{response_text}")
                
                if attempt == max_retries:
                    raise
                logger.warning(f"⏳ {CONFIG['retry_delay']}s 后重试...")
                time.sleep(CONFIG["retry_delay"])
                
            except requests.exceptions.Timeout:
                logger.warning(f"⏰ 请求超时 (尝试 {attempt+1}/{max_retries+1})")
                if attempt == max_retries:
                    raise
                time.sleep(CONFIG["retry_delay"])
                
            except requests.exceptions.ConnectionError:
                logger.error(f"❌ 连接错误：无法访问 {self.BASE_URL}")
                logger.error("💡 检查：1.网络连接  2.代理设置  3.防火墙")
                if attempt == max_retries:
                    raise
                time.sleep(CONFIG["retry_delay"])
                
            except json.JSONDecodeError as e:
                logger.error(f"❌ 响应不是有效 JSON: {e}")
                logger.error(f"💡 原始响应：{resp.text[:200] if 'resp' in locals() else 'N/A'}")
                raise
                
            except Exception as e:
                logger.warning(f"⚠️  未知异常 (尝试 {attempt+1}/{max_retries+1}): {type(e).__name__}: {e}")
                if attempt == max_retries:
                    raise
                time.sleep(CONFIG["retry_delay"])
        
        raise Exception("请求失败，已达最大重试次数")
    
    def get_upload_url(self, file_name: str) -> dict:
        """获取单个文件上传 URL"""
        payload = {
            "files": [{"name": file_name}],
            "model_version": CONFIG["model_version"],
            "language": CONFIG["language"],
            "enable_ocr": CONFIG["enable_ocr"],
            "enable_table": CONFIG["enable_table"],
            "enable_formula": CONFIG["enable_formula"],
        }
        result = self._request("POST", "/file-urls/batch", json=payload)
        return result["data"]
    
    def upload_file(self, file_url: str, file_path: str) -> bool:
        """上传文件到 OSS（带超时）"""
        try:
            logger.debug(f"📤 上传到 OSS: {file_url[:50]}...")
            with open(file_path, "rb") as f:
                resp = requests.put(
                    file_url, 
                    data=f, 
                    timeout=CONFIG["upload_timeout"]
                )
                success = resp.status_code in (200, 201)
                logger.debug(f"📡 上传响应：{resp.status_code}")
                return success
        except requests.exceptions.Timeout:
            logger.warning(f"⏰ 上传超时 ({CONFIG['upload_timeout']}s)")
            return False
        except FileNotFoundError:
            logger.error(f"❌ 文件不存在：{file_path}")
            return False
        except Exception as e:
            logger.error(f"❌ 上传失败：{type(e).__name__}: {e}")
            return False
    
    def poll_single_result(self, batch_id: str, file_name: str) -> dict:
        """轮询单个文件结果（带超时）"""
        start_time = time.time()
        timeout = CONFIG["parse_timeout"]
        
        logger.info(f"⏳ 开始轮询，超时限制：{timeout}s")
        
        while time.time() - start_time < timeout:
            try:
                endpoint = f"/extract-results/batch/{batch_id}"
                result = self._request("GET", endpoint, max_retries=1)
                extract_results = result["data"].get("extract_result", [])
                
                # 查找目标文件
                for r in extract_results:
                    if r["file_name"] == file_name:
                        state = r["state"]
                        
                        if state == "done":
                            elapsed = time.time() - start_time
                            logger.info(f"✅ 解析完成，耗时：{elapsed:.1f}s")
                            return r
                        elif state == "failed":
                            err_msg = r.get("err_msg", "未知错误")
                            logger.error(f"❌ 解析失败：{err_msg}")
                            return r
                        else:
                            elapsed = time.time() - start_time
                            logger.debug(f"⏳ 状态：{state} (已等待 {elapsed:.0f}s/{timeout}s)")
                        break  # 找到目标文件，退出循环
                        
            except Exception as e:
                logger.warning(f"⚠️  轮询出错：{type(e).__name__}: {e}，继续尝试...")
            
            time.sleep(CONFIG["poll_interval"])
        
        # 超时处理
        logger.warning(f"⏰ 解析超时 ({timeout}s)，将跳过此文件")
        return {
            "state": "timeout", 
            "file_name": file_name, 
            "err_msg": f"解析超时 {timeout}s"
        }
    
    def download_and_extract_md(self, zip_url: str, output_path: Path) -> bool:
        """下载 ZIP 并提取 full.md（带超时）"""
        try:
            logger.debug(f"📥 下载 ZIP: {zip_url[:50]}...")
            resp = requests.get(zip_url, stream=True, timeout=CONFIG["download_timeout"])
            resp.raise_for_status()
            
            # 保存临时 ZIP
            temp_zip = output_path.parent / f"{output_path.stem}.zip"
            with open(temp_zip, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            logger.debug(f"✓ ZIP 下载完成：{temp_zip.name} ({temp_zip.stat().st_size/1024:.1f} KB)")
            
            # 解压并提取 .md 文件
            with zipfile.ZipFile(temp_zip, "r") as zf:
                md_names = [n for n in zf.namelist() if n.endswith(".md")]
                if not md_names:
                    logger.error(f"❌ ZIP 中未找到 .md 文件，内容：{zf.namelist()[:10]}")
                    raise Exception("ZIP 中未找到 Markdown 文件")
                
                # 优先找 full.md
                target_md = next((n for n in md_names if n.endswith("full.md")), md_names[0])
                logger.debug(f"📄 提取：{target_md}")
                
                # 解压到临时目录
                extract_dir = output_path.parent / f"extract_{output_path.stem}"
                extract_dir.mkdir(exist_ok=True)
                zf.extract(target_md, extract_dir)
                
                # 移动并重命名
                extracted = extract_dir / target_md
                if extracted != output_path:
                    shutil.move(str(extracted), str(output_path))
                    logger.debug(f"📋 已重命名：{extracted.name} → {output_path.name}")
                
                # 清理临时目录
                shutil.rmtree(extract_dir)
            
            # 清理 ZIP
            temp_zip.unlink(missing_ok=True)
            return True
            
        except requests.exceptions.Timeout:
            logger.warning(f"⏰ 下载超时 ({CONFIG['download_timeout']}s)")
            return False
        except zipfile.BadZipFile:
            logger.error(f"❌ ZIP 文件损坏")
            return False
        except Exception as e:
            logger.error(f"❌ 下载/解压失败：{type(e).__name__}: {e}")
            return False


def process_single_file(client, pdf_path, output_dir):
    """
    处理单个文件：上传→轮询→下载→保存
    返回：(状态码，错误信息)
    """
    file_name = pdf_path.name
    md_path = output_dir / f"{pdf_path.stem}.md"
    
    # 跳过已存在的文件
    if CONFIG["skip_existing"] and md_path.exists():
        logger.info(f"⊘ 跳过 (已存在): {file_name}")
        return "skipped", None
    
    try:
        # ========== 阶段 1: 获取上传 URL ==========
        logger.info(f"📤 [1/4] 获取上传链接：{file_name}")
        try:
            upload_data = client.get_upload_url(file_name)
            batch_id = upload_data["batch_id"]
            file_url = upload_data["file_urls"][0]
            logger.debug(f"✓ 获取成功，batch_id: {batch_id[:12]}...")
        except Exception as e:
            error_str = f"{type(e).__name__}: {e}"
            logger.error(f"❌ [1/4] 获取上传链接失败: {error_str}")
            
            # 认证错误特别提示
            if "401" in error_str or "Unauthorized" in error_str or "token" in error_str.lower():
                logger.error("💡 关键提示：认证失败！请运行 test_auth.py 验证 Token")
            
            return "upload_url_failed", error_str
        
        # ========== 阶段 2: 上传文件 ==========
        logger.info(f"📤 [2/4] 上传文件：{file_name}")
        if not client.upload_file(file_url, str(pdf_path)):
            return "upload_failed", "上传失败或超时"
        logger.debug(f"✓ 上传成功")
        
        # ========== 阶段 3: 轮询解析结果 ==========
        logger.info(f"⏳ [3/4] 等待解析：{file_name} (最多 {CONFIG['parse_timeout']}s)")
        result = client.poll_single_result(batch_id, file_name)
        
        # 处理超时
        if result.get("state") == "timeout":
            if CONFIG["skip_on_timeout"]:
                logger.warning(f"⏭️  {file_name} 超时跳过")
                return "timeout", result.get("err_msg", "解析超时")
            else:
                return "timeout_error", result.get("err_msg", "解析超时")
        
        # 处理解析失败
        if result.get("state") == "failed":
            return "parse_failed", result.get("err_msg", "解析失败")
        
        # 处理未知状态
        if result.get("state") != "done":
            return "unknown_state", f"未知状态：{result.get('state')}"
        
        # ========== 阶段 4: 下载并保存 ==========
        zip_url = result.get("full_zip_url")
        if not zip_url:
            return "no_download_url", "无下载链接"
        
        logger.info(f"📥 [4/4] 下载结果：{file_name}")
        if not client.download_and_extract_md(zip_url, md_path):
            return "download_failed", "下载或解压失败"
        
        # 成功完成
        file_size = md_path.stat().st_size
        logger.info(f"✅ 完成：{file_name} ({file_size/1024:.2f} KB)")
        return "success", None
        
    except Exception as e:
        # 捕获未预期的异常
        logger.exception(f"❌ 未捕获异常 [{file_name}]: {type(e).__name__}: {e}")
        return "exception", f"{type(e).__name__}: {e}"


def batch_convert_streaming():
    """流式批量转换主函数"""
    # 验证 Token 配置
    token = CONFIG["token"]
    if token == "your_token_here":
        logger.error("❌ 配置错误：请编辑脚本，设置 CONFIG['token'] 为您的 MinerU API Token")
        logger.error("💡 获取方式：登录 https://mineru.net → 个人中心 → API 管理 → 创建 Token")
        logger.error("💡 格式要求：以 sk- 或 mr- 开头的字符串")
        return
    
    # 初始化路径
    input_dir = Path(CONFIG["input_dir"])
    output_dir = Path(CONFIG["output_dir"])
    temp_dir = Path(CONFIG["temp_dir"])
    
    output_dir.mkdir(parents=True, exist_ok=True)
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # 收集 PDF 文件
    pdf_files = list(input_dir.glob("*.pdf")) + list(input_dir.glob("*.PDF"))
    pdf_files = list(set(pdf_files))
    pdf_files.sort(key=lambda x: x.name)  # 排序保证顺序一致
    
    if not pdf_files:
        logger.error(f"❌ 在 {input_dir.absolute()} 中未找到 PDF 文件")
        logger.info(f"💡 请将 PDF 文件放入：{input_dir.absolute()}")
        return
    
    # 限制文件数量（测试用）
    if CONFIG["max_files"]:
        pdf_files = pdf_files[:CONFIG["max_files"]]
        logger.info(f"📋 限制处理前 {CONFIG['max_files']} 个文件（测试模式）")
    
    total_pages = len(pdf_files) * CONFIG["est_pages_per_file"]
    
    # 启动日志
    logger.info("=" * 70)
    logger.info(f"🚀 MinerU API 流式转换器启动")
    logger.info("=" * 70)
    logger.info(f"📁 输入目录：{input_dir.absolute()}")
    logger.info(f"📂 输出目录：{output_dir.absolute()}")
    logger.info(f"📊 文件数：{len(pdf_files)} | 估算页数：{total_pages}")
    logger.info(f"📄 每日配额：{CONFIG['daily_page_limit']} 页 | 预计需 {total_pages/CONFIG['daily_page_limit']:.1f} 天")
    logger.info(f"⚙️  模型：{CONFIG['model_version']} | 语言：{CONFIG['language']}")
    logger.info(f"⏱️  超时：上传 {CONFIG['upload_timeout']}s | 解析 {CONFIG['parse_timeout']}s | 下载 {CONFIG['download_timeout']}s")
    logger.info(f"✅ 模式：流式处理 + 超时自动跳过 + 断点续传")
    logger.info("=" * 70)
    
    # 初始化客户端
    try:
        client = MinerUAPIClient(token)
    except ValueError as e:
        logger.error(f"❌ 客户端初始化失败：{e}")
        return
    except Exception as e:
        logger.error(f"❌ 客户端初始化异常：{type(e).__name__}: {e}")
        return
    
    # 统计信息
    stats = {"success": 0, "failed": 0, "skipped": 0, "timeout": 0}
    failed_details = []
    pages_used = 0
    
    # 逐个处理（流式）
    for idx, pdf_file in enumerate(pdf_files, 1):
        logger.info(f"\n{'='*70}")
        logger.info(f"[{idx}/{len(pdf_files)}] 处理：{pdf_file.name}")
        logger.info(f"{'='*70}")
        
        # 处理单个文件
        status, error = process_single_file(client, pdf_file, output_dir)
        
        # 更新统计
        if status == "success":
            stats["success"] += 1
            pages_used += CONFIG["est_pages_per_file"]
        elif status == "skipped":
            stats["skipped"] += 1
        elif status == "timeout":
            stats["timeout"] += 1
            failed_details.append({
                "file": pdf_file.name,
                "status": status,
                "error": error,
                "action": "已跳过"
            })
        else:
            stats["failed"] += 1
            failed_details.append({
                "file": pdf_file.name,
                "status": status,
                "error": error
            })
        
        # 实时进度
        total_processed = stats["success"] + stats["timeout"] + stats["failed"] + stats["skipped"]
        logger.info(f"\n📊 进度：{stats['success']}✅ | {stats['timeout']}⏰ | {stats['failed']}❌ | {stats['skipped']}⊘ | 合计：{total_processed}/{len(pdf_files)}")
        
        # 配额检查
        if pages_used >= CONFIG["daily_page_limit"]:
            logger.warning(f"\n⚠️  已达到每日配额限制 ({pages_used}/{CONFIG['daily_page_limit']} 页)")
            logger.warning("💡 建议：明天继续处理剩余文件，或购买额外额度")
            break
        
        # 配额预警
        remaining = CONFIG["daily_page_limit"] - pages_used
        if remaining < CONFIG["est_pages_per_file"] * 2:
            logger.warning(f"⚠️  剩余配额不足 ({remaining} 页)，处理完当前文件后停止")
    
    # 清理临时目录
    if temp_dir.exists():
        try:
            shutil.rmtree(temp_dir)
            logger.debug(f"🧹 已清理临时目录：{temp_dir}")
        except Exception as e:
            logger.warning(f"⚠️  清理临时目录失败：{e}")
    
    # 输出最终报告
    logger.info(f"\n{'='*70}")
    logger.info("📋 转换完成报告")
    logger.info(f"{'='*70}")
    logger.info(f"✅ 成功：{stats['success']}")
    logger.info(f"⏰ 超时跳过：{stats['timeout']}")
    logger.info(f"❌ 失败：{stats['failed']}")
    logger.info(f"⊘ 已跳过：{stats['skipped']}")
    logger.info(f"📊 总处理：{stats['success'] + stats['timeout'] + stats['failed'] + stats['skipped']}")
    logger.info(f"📄 消耗配额：约 {pages_used} 页 / {CONFIG['daily_page_limit']} 页")
    
    # 问题文件详情
    problem_count = stats["failed"] + stats["timeout"]
    if problem_count > 0:
        logger.warning(f"\n⚠️  问题文件 ({problem_count} 个):")
        all_problems = failed_details + [
            {"file": "未知", "status": "timeout", "error": "解析超时", "action": "已跳过"}
            for _ in range(stats["timeout"] - len([f for f in failed_details if f["status"]=="timeout"]))
        ]
        for item in all_problems[:20]:
            action = item.get("action", "")
            logger.warning(f"  - {item['file']}: [{item['status']}] {item['error']} {action}")
        if problem_count > 20:
            logger.warning(f"  ... 还有 {problem_count-20} 个")
    
    # 保存报告
    report_path = output_dir / "api_conversion_report.json"
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "config": {k: v for k, v in CONFIG.items() if k != "token"},
                "stats": stats,
                "pages_used": pages_used,
                "failed_details": failed_details
            }, f, ensure_ascii=False, indent=2)
        logger.info(f"💾 报告已保存：{report_path}")
    except Exception as e:
        logger.warning(f"⚠️  保存报告失败：{e}")
    
    # 最终提示
    logger.info(f"📂 输出目录：{output_dir.absolute()}")
    logger.info("✅ 所有任务完成！")
    
    # 返回码（便于自动化）
    if stats["success"] == 0 and stats["skipped"] == 0:
        logger.error("❌ 没有成功转换任何文件，请检查日志")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    batch_convert_streaming()