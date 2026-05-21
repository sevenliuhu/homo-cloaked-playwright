# homo-cloaked-playwright 🛡️

> **Chromium隐身浏览器** — 100% Playwright兼容接口  
> 和 [invisible_playwright](https://github.com/feder-cr/invisible_playwright) 互补：Firefox版 → Chromium版

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CloakBrowser](https://img.shields.io/badge/engine-CloakBrowser%200.3.28-orange)](https://github.com/CloakHQ/CloakBrowser)

---

## Benchmark

| 检测工具 | 结果 | 对比 |
|:---------|:----|:-----|
| **Google reCAPTCHA v3** | **0.9/1.0** | 大多数方案0.3-0.7 |
| **FingerprintJS Pro** | **未检测到Bot** | VPN: false, 篡改: false |
| **CreepJS** | **0 谎言** | 指纹内部一致 |
| **SannySoft** | **全部通过** | WebDriver/Canvas/Font全部一致 |

## 快速开始

```bash
pip install cloaked-playwright
```

```python
from cloaked_playwright.sync_api import cloaked_sync
browser = cloaked_sync(url="https://example.com")
print(browser.snapshot())
browser.close()
```

**Firefox版搞不定的Chromium-only站点，交给这个。**

---

## 产品矩阵

| 项目 | 说明 |
|:-----|:------|
| [homo-cloaked-playwright](https://github.com/sevenliuhu/homo-cloaked-playwright) | ⬅️ 当前项目 |
| [homo-skyvern-integration](https://github.com/sevenliuhu/homo-skyvern-integration) | Skyvern + CloakBrowser 反爬补充 |
| [homo-native-feel-ext](https://github.com/sevenliuhu/homo-native-feel-ext) | 跨平台桌面设计扩展 |


---

## Business Contact

**HOMO AI Agent OS** — Not just an AI assistant, your entire AI team.

| Channel | Contact |
|:--------|:--------|
| Email | **16208204@qq.com** |
| Phone/WeChat | **13437576418** |
| GitHub | [sevenliuhu](https://github.com/sevenliuhu) |
| Services | Web Scraping, AI Agent Workflows, Web Dev, Brand Design, Short Video, Tech Solutions |

> For custom development or commercial license, contact us above. Response within 24h.
> This repository is for reference only. Commercial use requires a license.

