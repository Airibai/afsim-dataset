#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量 PDF 转 Markdown 转换器
使用 MinerU (MagicPDF) - Conda 环境版本
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==================== 配置区域 ====================
CONFIG = {
    "input_dir": "./pdf_files",           # PDF 输入目录
    "output_dir": "./markdown_files",      # Markdown 输出目录
    "max_workers": 4,                      # 并行线程数
    "enable_ocr": True,                    # 是否启用 OCR（扫描版 PDF）
    "page_limit": None,                    # 单文件页数限制（None 表示无限制）
    "skip_existing": True,                 # 是否跳过已存在的文件
    "log_file": "conversion_log.txt",      # 日志文件
}
# ================================================


def setup_logging(log_file):
    """配置日志系统"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)


def check_environment():
    """检查运行环境"""
    logger = logging.getLogger(__name__)
    
    # 检查 Python 版本
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    logger.info(f"Python 版本：{python_version}")
    
    if sys.version_info < (3, 9):
        logger.warning("⚠️  建议 Python 3.9+ 以获得最佳兼容性")
    
    # 检查 magic-pdf 是否安装
    try:
        import magic_pdf
        # 兼容不同版本的版本获取方式
        try:
            version = magic_pdf.__version__
        except AttributeError:
            # 尝试使用 importlib 获取版本
            from importlib.metadata import version, PackageNotFoundError
            try:
                version = version("magic-pdf")
            except PackageNotFoundError:
                version = "unknown"
        logger.info(f"MinerU 版本：{version}")
    except ImportError:
        logger.error("❌ 未找到 magic-pdf，请先安装：pip install magic-pdf[full]")
        return False
    
    # 检查可选依赖
    try:
        import unimernet
        logger.info("✓ 公式识别模块 (unimernet) 已安装")
    except ImportError:
        logger.warning("⚠️  公式识别模块 (unimernet) 未安装，公式可能解析不完整")
    
    return True


class PDFConverter:
    """PDF 转换类"""
    
    def __init__(self, config):
        self.config = config
        self.input_dir = Path(config["input_dir"])
        self.output_dir = Path(config["output_dir"])
        self.logger = logging.getLogger(__name__)
        
        # 统计信息
        self.stats = {
            "total": 0,
            "success": 0,
            "failed": 0,
            "skipped": 0,
            "failed_files": []
        }
        
        # 创建输出目录
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 配置 MinerU 模型
        self._setup_mineru()
    
    def _setup_mineru(self):
        """配置 MinerU 模型参数"""
        try:
            import magic_pdf.model as model_config
            
            # 启用内部模型
            model_config.__use_inside_model__ = True
            
            # 是否启用 OCR
            if self.config["enable_ocr"]:
                model_config.__model_mode__ = "ocr"
                self.logger.info("✓ OCR 模式已启用")
            else:
                model_config.__model_mode__ = "layout"
                self.logger.info("✓ 布局分析模式已启用")
                
        except Exception as e:
            self.logger.warning(f"模型配置警告：{e}")
    
    def convert_single(self, pdf_path):
        """转换单个 PDF 文件"""
        pdf_path = Path(pdf_path)
        md_filename = pdf_path.stem + ".md"
        md_path = self.output_dir / md_filename
        
        # 检查是否跳过
        if self.config["skip_existing"] and md_path.exists():
            self.logger.info(f"⊘ 跳过 (已存在): {pdf_path.name}")
            self.stats["skipped"] += 1
            return True
        
        try:
            self.logger.info(f"▶ 开始：{pdf_path.name}")
            
            # 导入转换函数
            from magic_pdf.libs.convert import convert_pdf_to_md
            
            # 执行转换
            convert_pdf_to_md(
                pdf_path=str(pdf_path.absolute()),
                output_dir=str(self.output_dir.absolute()),
                is_json_md_dump=True,
                is_debug=False,
                page_count_limit=self.config["page_limit"]
            )
            
            # 验证结果
            if md_path.exists():
                file_size = md_path.stat().st_size
                self.logger.info(f"✓ 成功：{md_filename} ({file_size/1024:.2f} KB)")
                self.stats["success"] += 1
                return True
            else:
                raise Exception("转换后文件未生成")
                
        except Exception as e:
            self.logger.error(f"✗ 失败：{pdf_path.name} - {str(e)}")
            self.stats["failed"] += 1
            self.stats["failed_files"].append({
                "file": pdf_path.name,
                "error": str(e)
            })
            return False
    
    def batch_convert(self):
        """批量转换"""
        # 收集 PDF 文件
        pdf_files = []
        for ext in ["*.pdf", "*.PDF"]:
            pdf_files.extend(self.input_dir.glob(ext))
        pdf_files = list(set(pdf_files))
        
        if not pdf_files:
            self.logger.warning(f"⚠️  在 {self.input_dir} 中未找到 PDF 文件")
            return False
        
        self.stats["total"] = len(pdf_files)
        self.logger.info("=" * 60)
        self.logger.info(f"共找到 {self.stats['total']} 个 PDF 文件")
        self.logger.info(f"并行线程数：{self.config['max_workers']}")
        self.logger.info("=" * 60)
        
        # 并行处理
        with ThreadPoolExecutor(max_workers=self.config["max_workers"]) as executor:
            futures = {executor.submit(self.convert_single, f): f for f in pdf_files}
            
            for idx, future in enumerate(as_completed(futures), 1):
                progress = f"[{idx}/{self.stats['total']}]"
                self.logger.info(f"{progress} 进度：{idx/self.stats['total']*100:.1f}%")
        
        # 输出报告
        self._generate_report()
        return True
    
    def _generate_report(self):
        """生成转换报告"""
        self.logger.info("=" * 60)
        self.logger.info("转换完成报告")
        self.logger.info("=" * 60)
        self.logger.info(f"总文件数：{self.stats['total']}")
        self.logger.info(f"成功：{self.stats['success']}")
        self.logger.info(f"失败：{self.stats['failed']}")
        self.logger.info(f"跳过：{self.stats['skipped']}")
        
        if self.stats["total"] > 0:
            success_rate = self.stats["success"] / self.stats["total"] * 100
            self.logger.info(f"成功率：{success_rate:.2f}%")
        
        if self.stats["failed_files"]:
            self.logger.warning("\n失败文件详情:")
            for item in self.stats["failed_files"]:
                self.logger.warning(f"  - {item['file']}: {item['error']}")
        
        # 保存 JSON 报告
        report_path = self.output_dir / "conversion_report.json"
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "config": self.config,
            "stats": self.stats
        }
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)
        
        self.logger.info(f"\n报告已保存：{report_path}")


def main():
    """主函数"""
    # 设置日志
    logger = setup_logging(CONFIG["log_file"])
    
    # 检查环境
    logger.info("正在检查运行环境...")
    if not check_environment():
        sys.exit(1)
    
    # 检查输入目录
    input_path = Path(CONFIG["input_dir"])
    if not input_path.exists():
        logger.info(f"创建输入目录：{input_path.absolute()}")
        input_path.mkdir(parents=True, exist_ok=True)
        logger.warning(f"⚠️  请将 PDF 文件放入：{input_path.absolute()}")
        logger.warning("然后重新运行此脚本")
        sys.exit(0)
    
    # 执行转换
    logger.info("开始批量转换...")
    converter = PDFConverter(CONFIG)
    converter.batch_convert()
    
    logger.info("\n" + "=" * 60)
    logger.info("所有任务完成！")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()