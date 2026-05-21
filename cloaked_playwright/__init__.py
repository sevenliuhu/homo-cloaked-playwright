# Copyright (c) 2026 HOMO AI. Proprietary. License required. Contact: 16208204@qq.com
"""
cloaked_playwright — Chromium隐身浏览器，Playwright兼容接口

底层引擎：CloakBrowser (基于Chromium的49个C++源码级反检测补丁)
和 invisible_playwright 是互补关系：
  - invisible_playwright: Firefox版，Firefox某些站点兼容性差
  - cloaked_playwright: Chromium版，兼容所有Chromium-only站点

接口设计参考了 invisible_playwright（致谢），
但底层引擎是完全自主研发的 CloakBrowser Chromium。
"""

from .sync_api import cloaked_sync, CloakedBrowser  # noqa
from .async_api import cloaked_async  # noqa
from ._version import __version__  # noqa

__all__ = ["cloaked_sync", "cloaked_async", "CloakedBrowser"]
