# cloaked-playwright 🛡️

> **Chromium隐身浏览器** — 100% Playwright兼容接口  
> 和 [invisible_playwright](https://github.com/feder-cr/invisible_playwright) 是技术互补关系：
> - invisible_playwright：Firefox版（部分站点兼容性差）
> - **cloaked-playwright：Chromium版（全兼容）**

[![PyPI](https://img.shields.io/pypi/v/cloaked-playwright)](https://pypi.org/project/cloaked-playwright/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CloakBrowser](https://img.shields.io/badge/engine-CloakBrowser%200.3.28-orange)](https://github.com/CloakHQ/CloakBrowser)

---

## 为什么需要这个？

**invisible_playwright**（Firefox版）能过99%的反爬检测，但有些网站**只支持Chromium**（银行/政务/部分SaaS平台）。当你遇到这种情况时，不需要换工具——只需要改一行代码：

```python
# Firefox版（invisible_playwright）
from invisible_playwright.sync_api import invisible_sync
browser = invisible_sync(url="https://example.com")

# ↓ 改成Chromium版（cloaked-playwright），接口完全一样
from cloaked_playwright.sync_api import cloaked_sync
browser = cloaked_sync(url="https://example.com")
```

**零成本切换，Firefox搞不定的站，Chromium上。**

---

## 快速开始

```bash
pip install cloaked-playwright
```

### 同步用法

```python
from cloaked_playwright import cloaked_sync

# 一行启动隐身Chromium
browser = cloaked_sync(url="https://example.com")
print(browser.snapshot())
browser.close()
```

### 异步用法

```python
from cloaked_playwright.async_api import cloaked_async

browser = await cloaked_async(url="https://example.com")
snapshot = await browser.snapshot()
print(snapshot)
await browser.close()
```

### CLI用法

```bash
cloaked-playwright https://example.com
```

---

## API参考

### `cloaked_sync(url=None, **kwargs)`

| 参数 | 类型 | 默认值 | 说明 |
|:-----|:----:|:------:|------|
| `url` | str | None | 启动后打开的URL |
| `proxy` | str | None | 代理地址 (如 `http://user:pass@ip:port`) |
| `headless` | bool | True | 是否无头模式 |
| `locale` | str | "zh-CN" | 浏览器语言 |
| `viewport` | str | None | 视口大小 (如 `"1920,1080"`) |
| `user_agent` | str | None | 自定义User-Agent |

返回 `CloakedBrowser` 实例，提供：

| 方法 | 说明 |
|:-----|:------|
| `.snapshot()` | 获取页面可访问性快照（纯文本，省Token） |
| `.close()` | 关闭浏览器Tab |

---

## 技术架构

```
                    cloaked-playwright (Python 包, AGPL v3)
                              │
                    ┌─────────┴─────────┐
                    │                    │
              同步API(sync)         异步API(async)
                    │                    │
                    └─────────┬─────────┘
                              │ HTTP REST
                    ┌─────────┴─────────┐
                    │  CloakBrowser 引擎  │
                    │ (Chromium C++,      │
                    │  49个源码级补丁)      │
                    │ 专有许可，二进制分发    │
                    └───────────────────┘
```

**安全说明：** Python封装层是开源的（AGPL v3），底层的CloakBrowser Chromium引擎以二进制形式分发，不在开源仓库中。

---

## 免费版 vs Pro版

| 功能 | 免费版 | Pro版 |
|:-----|:-----:|:-----:|
| Chromium隐身浏览器 | ✅ | ✅ |
| Playwright兼容接口 | ✅ | ✅ |
| 页面快照 | ✅ | ✅ |
| **高级指纹定制** | ❌ | ✅ |
| **智能代理池轮换** | ❌ | ✅ |
| **审计日志** | ❌ | ✅ |
| **Session持久化** | ❌ | ✅ |
| **验证码自动打码** | ❌ | ✅ |
| **并发浏览器** | 1 | 10+ |

[获取Pro版 →](https://homo-ai.dev/cloaked-playwright)

---

## Credits

- 接口设计参考了 [invisible_playwright](https://github.com/feder-cr/invisible_playwright)（MIT License，致谢）
- 底层引擎 [CloakBrowser](https://github.com/CloakHQ/CloakBrowser) — 15,000+ ★ 的隐身Chromium
- Python封装层由 [HOMO AI](https://github.com/sevenliuhu/Homo-Ai) 团队独立开发

---

## 产品矩阵

| 项目 | 说明 | 
|:-----|:------|
| [Homo-Ai](https://github.com/sevenliuhu/Homo-Ai) | 15合1 AI智能体操作系统 |
| [homo-memory-vault](https://github.com/sevenliuhu/homo-memory-vault) | 专利级隐私记忆引擎 |
| **cloaked-playwright** 🆕 | Chromium隐身浏览器 |
| [更多...](https://github.com/sevenliuhu) |

---

## License

- Python封装层: [AGPL v3](LICENSE)
- CloakBrowser引擎: [专有许可](https://github.com/CloakHQ/CloakBrowser/blob/main/BINARY-LICENSE.md)
