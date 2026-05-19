"""
cloaked_playwright.async_api — 异步API，接口对齐invisible_playwright

用法:
    from cloaked_playwright.async_api import cloaked_async
    browser = await cloaked_async(url="https://example.com")
"""
import json
import logging
from typing import Optional

from .constants import DEFAULT_API_HOST, DEFAULT_TIMEOUT

logger = logging.getLogger("cloaked_playwright")


class AsyncCloakedBrowser:
    """异步CloakedBrowser — 接口对齐invisible_playwright的异步版"""

    def __init__(self, tab_id: str, api_host: str = DEFAULT_API_HOST):
        self._tab_id = tab_id
        self._api_host = api_host
        self._closed = False

    async def snapshot(self, max_chars: int = 5000) -> str:
        """获取快照"""
        if self._closed:
            raise RuntimeError("Browser already closed")
        return await self._async_api("GET", f"/tabs/snapshot?tabId={self._tab_id}")

    async def close(self):
        if self._closed:
            return
        try:
            await self._async_api("POST", "/tabs/close", {"tabId": self._tab_id})
        except Exception:
            pass
        self._closed = True

    async def _async_api(self, method: str, path: str, body: dict = None):
        import aiohttp
        url = f"{self._api_host}{path}"
        async with aiohttp.ClientSession() as session:
            if method == "GET":
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as resp:
                    return await resp.json()
            else:
                async with session.post(url, json=body, timeout=aiohttp.ClientTimeout(total=30)) as resp:
                    return await resp.json()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()


async def cloaked_async(url: Optional[str] = None, **kwargs):
    """
    启动隐身Chromium浏览器（异步版）
    
    接口对齐 invisible_playwright.async_api.invisible_async()
    
    用法:
        browser = await cloaked_async(url="https://example.com")
        print(await browser.snapshot())
        await browser.close()
    """
    import aiohttp
    api_host = kwargs.get("api_host", DEFAULT_API_HOST)
    
    payload = {"url": url or "about:blank", "config": {
        "headless": kwargs.get("headless", True),
        "locale": kwargs.get("locale", "zh-CN"),
    }}
    if kwargs.get("proxy"):
        payload["config"]["proxy"] = kwargs["proxy"]
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{api_host}/tabs/open",
            json=payload,
            timeout=aiohttp.ClientTimeout(total=30)
        ) as resp:
            result = await resp.json()
    
    tab_id = result.get("tabId")
    if not tab_id:
        raise RuntimeError(f"Failed to open browser: {result}")
    
    return AsyncCloakedBrowser(tab_id, api_host)
