"""常量配置 — 接口对齐参考了invisible_playwright"""
import os

# 默认scraper-server地址
DEFAULT_API_HOST = os.environ.get("HOMO_SCRAPER_HOST", "http://127.0.0.1:9377")
DEFAULT_TIMEOUT = int(os.environ.get("HOMO_SCRAPER_TIMEOUT", "30000"))

# 浏览器配置
CLOAKED_CHROMIUM_DIR = os.environ.get(
    "CLOAKED_CHROMIUM_DIR",
    os.path.expanduser("~/.cloaked-playwright/chromium")
)

# 代理配置
PROXY_ENABLED = os.environ.get("CLOAKED_PROXY_ENABLED", "").lower() in ("1", "true", "yes")
PROXY_LIST_PATH = os.environ.get("CLOAKED_PROXY_LIST", "")

# 高级功能开关（Pro版）
PRO_FEATURES = {
    "advanced_fingerprinting": False,  # Pro: 高级指纹定制
    "proxy_pool": False,               # Pro: 智能代理池
    "audit_log": False,                # Pro: 审计日志
    "session_persistence": False,      # Pro: Session持久化
    "captcha_solver": False,           # Pro: 验证码自动打码
    "concurrent_browsers": 1,          # Pro: 并发浏览器数
}
