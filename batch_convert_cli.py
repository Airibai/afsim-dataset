#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AFSIM PDF 批量转换器 (CLI 调用版)
适配 MinerU 1.3.12+ 参数规范 - 修复版
"""

import os
import sys
import subprocess
import shutil
import json
import logging
from pathlib import Path
from datetime import datetime

# ==================== 配置区域 ====================
CONFIG = {
    "input_dir": "./pdf_files",
    "output_dir": "./markdown_files",
    "method": "ocr",
    "lang": "ch",
    "skip_existing": True,
    "cleanup_temp": True,
    "debug": False,
}
# ================================================

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('conversion_log.txt', encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

def convert_single_cli(pdf_path, output_dir, method="ocr", lang="ch", debug=False):
    pdf_path = Path(pdf_path)
    pdf_name = pdf_path.stem
    
    cmd = [
        "magic-pdf",
        "-p", str(pdf_path.absolute()),
        "-o", str(Path(output_dir).absolute()),
        "-m", method,
    ]
    
    if lang:
        cmd.extend(["-l", lang])
    if debug:
        cmd.extend(["-d", "true"])
    
    try:
        logger.debug(f"执行命令：{' '.join(cmd)}")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=3600,
            encoding='utf-8',
            errors='ignore'
        )
        
        if result.returncode != 0:
            error_msg = result.stderr[:300] if result.stderr else "未知错误"
            return False, f"CLI 执行失败：{error_msg}"
        
        # 查找生成的 Markdown 文件
        possible_paths = [
            Path(output_dir) / pdf_name / "auto" / f"{pdf_name}.md",
            Path(output_dir) / pdf_name / f"{pdf_name}.md",
            Path(output_dir) / "auto" / pdf_name / f"{pdf_name}.md",
        ]
        
        found_md = None
        for p in possible_paths:
            if p.exists():
                found_md = p
                break
        
        if not found_md:
            search_dirs = [
                Path(output_dir) / pdf_name / "auto",
                Path(output_dir) / pdf_name,
                Path(output_dir) / "auto" / pdf_name,
            ]
            for search_dir in search_dirs:
                if search_dir.exists():
                    md_files = list(search_dir.glob("*.md"))
                    if md_files:
                        found_md = md_files[0]
                        break
        
        if found_md:
            final_path = Path(output_dir) / f"{pdf_name}.md"
            if found_md != final_path:
                shutil.copy2(found_md, final_path)
            
            temp_dir = Path(output_dir) / pdf_name
            if temp_dir.exists() and CONFIG.get("cleanup_temp", True):
                try:
                    shutil.rmtree(temp_dir)
                except Exception as e:
                    logger.warning(f"清理临时目录失败：{e}")
            
            file_size = final_path.stat().st_size
            return True, f"成功 ({file_size/1024:.2f} KB)"
        else:
            return False, "未找到生成的 Markdown 文件"
            
    except subprocess.TimeoutExpired:
        return False, "执行超时 (超过 1 小时)"
    except Exception as e:
        return False, str(e)


def batch_convert():
    input_dir = Path(CONFIG["input_dir"])
    output_dir = Path(CONFIG["output_dir"])
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    pdf_files = list(input_dir.glob("*.pdf")) + list(input_dir.glob("*.PDF"))
    pdf_files = list(set(pdf_files))
    
    if not pdf_files:
        logger.error(f"❌ 在 {input_dir} 中未找到 PDF 文件")
        return
    
    logger.info("=" * 60)
    logger.info(f"共找到 {len(pdf_files)} 个 PDF 文件")
    logger.info(f"解析方法：{CONFIG['method']}")
    logger.info(f"OCR 语言：{CONFIG['lang'] or 'auto'}")
    logger.info(f"输出目录：{output_dir.absolute()}")
    logger.info("=" * 60)
    
    stats = {"success": 0, "failed": 0, "skipped": 0}
    failed_files = []
    
    for idx, pdf_file in enumerate(pdf_files, 1):
        md_path = output_dir / f"{pdf_file.stem}.md"
        
        if CONFIG["skip_existing"] and md_path.exists():
            logger.info(f"[{idx}/{len(pdf_files)}] ⊘ 跳过：{pdf_file.name}")
            stats["skipped"] += 1
            continue
        
        logger.info(f"[{idx}/{len(pdf_files)}] ▶ 处理：{pdf_file.name}")
        
        success, msg = convert_single_cli(
            pdf_file,
            output_dir,
            method=CONFIG["method"],
            lang=CONFIG["lang"],
            debug=CONFIG["debug"]
        )
        
        if success:
            logger.info(f"✓ {msg}")
            stats["success"] += 1
        else:
            logger.error(f"✗ {msg}")
            stats["failed"] += 1
            failed_files.append({"file": pdf_file.name, "error": msg})
    
    # 输出报告
    logger.info("=" * 60)
    logger.info("转换完成报告")
    logger.info("=" * 60)
    logger.info(f"成功：{stats['success']}")
    logger.info(f"失败：{stats['failed']}")
    logger.info(f"跳过：{stats['skipped']}")
    
    # 修复：计算成功率（不用海象运算符）
    total_count = stats["success"] + stats["failed"] + stats["skipped"]
    if total_count > 0:
        rate = stats["success"] / total_count * 100
        logger.info(f"成功率：{rate:.2f}%")
    
    if failed_files:
        logger.warning("\n失败文件列表:")
        for item in failed_files:
            logger.warning(f"  - {item['file']}: {item['error']}")
    
    # 保存报告
    report_path = output_dir / "conversion_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "config": CONFIG,
            "stats": stats,
            "failed_files": failed_files
        }, f, ensure_ascii=False, indent=2)
    
    logger.info(f"\n报告已保存：{report_path}")


if __name__ == "__main__":
    try:
        result = subprocess.run(["magic-pdf", "--version"], capture_output=True, text=True, timeout=10)
        version = result.stdout.strip() or "unknown"
        logger.info(f"✓ magic-pdf CLI 已就绪 (版本：{version})")
    except FileNotFoundError:
        logger.error("❌ 未找到 magic-pdf 命令")
        sys.exit(1)
    
    batch_convert()