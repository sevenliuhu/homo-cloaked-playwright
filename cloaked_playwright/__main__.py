# Copyright (c) 2026 HOMO AI. Proprietary. License required. Contact: 16208204@qq.com
#!/usr/bin/env python3
"""cloaked-playwright CLI — 快速启动隐身浏览器"""
import sys
import json
from .sync_api import cloaked_sync


def main():
    args = sys.argv[1:]
    url = args[0] if args and not args[0].startswith("--") else None
    
    # 解析参数
    kwargs = {}
    for i, a in enumerate(sys.argv):
        if a == "--proxy" and i + 1 < len(sys.argv):
            kwargs["proxy"] = sys.argv[i + 1]
        elif a == "--no-headless":
            kwargs["headless"] = False
        elif a == "--locale" and i + 1 < len(sys.argv):
            kwargs["locale"] = sys.argv[i + 1]
        elif a == "--timeout" and i + 1 < len(sys.argv):
            kwargs["timeout"] = int(sys.argv[i + 1])
    
    try:
        browser = cloaked_sync(url, **kwargs)
        snapshot = browser.snapshot()
        print(json.dumps({"status": "ok", "tabId": browser.tab_id, "snapshot": snapshot}, indent=2))
        browser.close()
    except RuntimeError as e:
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
