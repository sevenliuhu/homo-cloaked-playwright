# Copyright (c) 2026 HOMO AI. Proprietary. License required. Contact: 16208204@qq.com
"""
cloaked_playwright.sync_api — 同步API，接口对齐invisible_playwright

零成本切换：
  from invisible_playwright.sync_api import invisible_sync
  → 改成：
  from cloaked_playwright.sync_api import cloaked_sync

底层是完全自主研发的CloakBrowser Chromium引擎，
不是Firefox，解决Firefox兼容性盲区。
"""
import json
import urllib.request
import urllib.error
import logging
from typing import Optional, Dict, Any

from .constants import DEFAULT_API_HOST, DEFAULT_TIMEOUT

logger = logging.getLogger("cloaked_playwright")


class CloakedBrowser:
    """
    CloakedBrowser实例 — 封装了一个隐身浏览器Tab
    
    接口对齐invisible_playwright的返回对象，
    但底层是CloakBrowser Chromium，不是Firefox。
    """

    def __init__(self, tab_id: str, api_host: str = DEFAULT_API_HOST):
        self._tab_id = tab_id
        self._api_host = api_host
        self._closed = False

    @property
    def tab_id(self) -> str:
        return self._tab_id

    def snapshot(self, max_chars: int = 5000) -> str:
        """获取当前页面快照（可访问性树）"""
        if self._closed:
            raise RuntimeError("Browser already closed")
        return self._api("GET", f"/tabs/snapshot?tabId={self._tab_id}&maxChars={max_chars}")

    def close(self):
        """关闭浏览器Tab"""
        if self._closed:
            return
        try:
            self._api("POST", "/tabs/close", {"tabId": self._tab_id})
        except Exception:
            pass
        self._closed = True

    def _api(self, method: str, path: str, body: dict = None) -> Any:
        url = f"{self._api_host}{path}"
        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(
            url, data=data,
            headers={"Content-Type": "application/json", "User-Agent": "cloaked-playwright/0.1"},
            method=method
        )
        try:
            with urllib.request.urlopen(req, timeout=DEFAULT_TIMEOUT / 1000) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"Engine error: {e.code} {e.reason}")
        except urllib.error.URLError as e:
            raise RuntimeError(f"Cannot reach engine: {e.reason}")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def cloaked_sync(url: Optional[str] = None, **kwargs) -> CloakedBrowser:
    """
    启动隐身Chromium浏览器（同步版）
    
    接口对齐 invisible_playwright.sync_api.invisible_sync()
    
    参数:
        url: 可选，打开指定URL
        **kwargs: 
            proxy: 代理地址 (如 "http://user:pass@ip:port")
            headless: 是否无头模式 (默认True)
            user_agent: 自定义UA
            viewport: 视口大小 (如 "1920,1080")
            locale: 语言 (如 "zh-CN")
            timeout: 超时毫秒
    
    返回:
        CloakedBrowser实例
    
    用法:
        from cloaked_playwright import cloaked_sync
        browser = cloaked_sync(url="https://example.com")
        print(browser.snapshot())
        browser.close()
    """
    api_host = kwargs.get("api_host", DEFAULT_API_HOST)
    
    # 构建浏览器配置
    browser_config = {
        "headless": kwargs.get("headless", True),
        "locale": kwargs.get("locale", "zh-CN"),
    }
    if kwargs.get("proxy"):
        browser_config["proxy"] = kwargs["proxy"]
    if kwargs.get("user_agent"):
        browser_config["userAgent"] = kwargs["user_agent"]
    if kwargs.get("viewport"):
        parts = kwargs["viewport"].split(",")
        if len(parts) == 2:
            browser_config["viewport"] = {"width": int(parts[0]), "height": int(parts[1])}
    
    # 通过API打开页面
    try:
        from urllib.request import Request, urlopen
        req = Request(
            f"{api_host}/tabs/open",
            data=json.dumps({"url": url or "about:blank", "config": browser_config}).encode(),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode())
    except Exception as e:
        raise RuntimeError(
            f"Engine unavailable: {e}. "
            "Make sure HOMO Scraper is running (port 9377). "
            "Or set HOMO_SCRAPER_HOST env var."
        )
    
    tab_id = result.get("tabId")
    if not tab_id:
        raise RuntimeError(f"Failed to open browser: {result}")
    
    return CloakedBrowser(tab_id, api_host)
