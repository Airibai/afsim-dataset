#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智谱 GLM API 客户端 - 支持流式/非流式、重试、错误处理
"""

import time
import json
import logging
from typing import List, Dict, Optional, Iterator
import requests

from config import config

logger = logging.getLogger(__name__)


class GLMClient:
    """智谱 GLM API 客户端"""
    
    def __init__(self, api_config=None):
        self.cfg = api_config or config.api
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.cfg.api_key}",
            "Content-Type": "application/json"
        })
        self._request_count = 0
        self._total_tokens = 0
    
    def _build_payload(self, messages: List[dict], stream: bool = False) -> dict:
        """构建请求体"""
        return {
            "model": self.cfg.model,
            "messages": messages,
            "stream": stream,
            "temperature": self.cfg.temperature,
            "top_p": self.cfg.top_p,
            "max_tokens": self.cfg.max_tokens,
        }
    
    def _request_with_retry(self, method: str, url: str, **kwargs) -> requests.Response:
        """带重试的 HTTP 请求"""
        last_error = None
        
        for attempt in range(self.cfg.max_retries + 1):
            try:
                resp = self.session.request(
                    method, url,
                    timeout=self.cfg.timeout,
                    **kwargs
                )
                resp.raise_for_status()
                return resp
                
            except requests.exceptions.Timeout as e:
                last_error = f"超时 ({self.cfg.timeout}s)"
                logger.warning(f"⚠️  请求超时 (尝试 {attempt+1}/{self.cfg.max_retries+1}): {e}")
                
            except requests.exceptions.ConnectionError as e:
                last_error = "连接错误"
                logger.error(f"❌ 连接失败 (尝试 {attempt+1}/{self.cfg.max_retries+1}): {e}")
                
            except requests.exceptions.HTTPError as e:
                status = e.response.status_code
                last_error = f"HTTP {status}"
                
                # 解析错误信息
                try:
                    error_body = e.response.json()
                    msg = error_body.get("error", {}).get("message", "")
                    last_error += f": {msg}"
                    
                    # 特殊错误处理
                    if status == 401:
                        logger.error("❌ 401: API Key 无效或过期")
                        break  # 不重试
                    elif status == 429:
                        logger.warning("⚠️  429: 请求频率超限，等待后重试")
                    elif status >= 500:
                        logger.warning(f"⚠️  {status}: 服务器错误，重试...")
                        
                except:
                    pass
                
            except Exception as e:
                last_error = f"{type(e).__name__}: {e}"
                logger.warning(f"⚠️  未知错误 (尝试 {attempt+1}/{self.cfg.max_retries+1}): {e}")
            
            # 重试前等待
            if attempt < self.cfg.max_retries:
                wait_time = self.cfg.retry_delay * (attempt + 1)
                logger.info(f"⏳ 等待 {wait_time:.1f}s 后重试...")
                time.sleep(wait_time)
        
        raise requests.exceptions.RequestException(f"请求失败 ({last_error})，已达最大重试次数")
    
    def chat(self, messages: List[dict]) -> Dict:
        """
        非流式对话（用于关键内容总结等短文本）
        
        Returns:
            dict: {"content": str, "usage": dict}
        """
        url = f"{self.cfg.api_base}/chat/completions"
        payload = self._build_payload(messages, stream=False)
        
        try:
            resp = self._request_with_retry("POST", url, json=payload)
            result = resp.json()
            
            # 提取内容
            content = result["choices"][0]["message"]["content"]
            usage = result.get("usage", {})
            
            # 统计
            self._request_count += 1
            self._total_tokens += usage.get("total_tokens", 0)
            
            return {"content": content, "usage": usage}
            
        except Exception as e:
            logger.error(f"❌ 对话请求失败：{e}")
            raise
    
    def chat_stream(self, messages: List[dict]) -> Iterator[str]:
        """
        流式对话生成器（用于数据集生成）
        
        Yields:
            str: 模型生成的文本片段
        """
        url = f"{self.cfg.api_base}/chat/completions"
        payload = self._build_payload(messages, stream=True)
        
        try:
            resp = self._request_with_retry("POST", url, json=payload, stream=True)
            
            full_content = ""
            usage = None
            
            for line in resp.iter_lines(decode_unicode=True):
                line = line.strip()
                if not line or line.startswith(":"):
                    continue
                if line == "data: [DONE]":
                    break
                if line.startswith("data: "):
                    try:
                        chunk = json.loads(line[6:])
                        delta = chunk.get("choices", [{}])[0].get("delta", {})
                        content = delta.get("content", "")
                        if content:
                            full_content += content
                            yield content
                        if "usage" in chunk:
                            usage = chunk["usage"]
                    except json.JSONDecodeError:
                        continue
            
            # 统计
            self._request_count += 1
            if usage:
                self._total_tokens += usage.get("total_tokens", 0)
                
        except Exception as e:
            logger.error(f"❌ 流式请求失败：{e}")
            yield f"\n❌ 请求错误：{e}"
    
    def get_stats(self) -> dict:
        """获取调用统计"""
        return {
            "request_count": self._request_count,
            "total_tokens": self._total_tokens,
            "estimated_cost_cny": self._total_tokens / 1000 * 0.02  # 估算：¥0.02/1k tokens
        }