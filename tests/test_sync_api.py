"""测试 cloaked-playwright 同步API"""
import pytest
from cloaked_playwright.sync_api import cloaked_sync, CloakedBrowser


class TestCloakedSync:
    def test_import(self):
        assert callable(cloaked_sync)

    def test_browser_interface(self):
        methods = ['snapshot', 'close', '__enter__', '__exit__']
        for m in methods:
            assert hasattr(CloakedBrowser, m), f"Missing: {m}"

    def test_error_handling(self):
        with pytest.raises(RuntimeError) as exc:
            cloaked_sync(api_host="http://127.0.0.1:1")
        assert "Engine unavailable" in str(exc.value)
