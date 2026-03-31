#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日志配置模块 - 结构化输出 + 文件轮转
"""

import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

from config import config


def setup_logger(name: str = "afsim_builder", log_file: Path = None) -> logging.Logger:
    """
    配置日志器
    
    特性：
    - 控制台：INFO 级别，彩色输出（如果支持）
    - 文件：DEBUG 级别，轮转存储（10MB × 5 份）
    - 格式：时间 + 级别 + 模块 + 消息
    """
    log_file = log_file or config.paths.log_file
    
    # 创建 logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # 根级别最低，由 handler 控制
    
    # 清除旧 handlers（避免重复）
    logger.handlers = []
    
    # 格式化器
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    
    # 文件 Handler（轮转）
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5,
        encoding='utf-8',
        delay=True  # 延迟打开，避免空文件
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    
    # 控制台 Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)  # 控制台只显示重要信息
    console_handler.setFormatter(console_formatter)
    
    # 添加 handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    # 捕获 requests 等库的冗余日志
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    
    return logger


# 全局 logger 实例
logger = setup_logger()


def get_logger(name: str) -> logging.Logger:
    """获取子模块 logger"""
    return logging.getLogger(f"afsim_builder.{name}")