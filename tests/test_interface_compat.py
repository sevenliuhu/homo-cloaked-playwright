"""接口兼容性测试 — 验证和invisible_playwright的接口对齐"""


class TestInterfaceCompat:
    """验证 cloaked_playwright 接口和 invisible_playwright 对齐"""

    def test_sync_api_import_path(self):
        """invisible_playwright: from invisible_playwright.sync_api import invisible_sync"""
        from cloaked_playwright.sync_api import cloaked_sync
        assert callable(cloaked_sync)

    def test_async_api_import_path(self):
        """invisible_playwright: from invisible_playwright.async_api import invisible_async"""
        from cloaked_playwright.async_api import cloaked_async
        import inspect
        assert inspect.iscoroutinefunction(cloaked_async)

    def test_top_level_imports(self):
        """验证顶层导入"""
        import cloaked_playwright
        assert hasattr(cloaked_playwright, 'cloaked_sync')
        assert hasattr(cloaked_playwright, 'CloakedBrowser')

    def test_sync_api_params(self):
        """验证同步API参数名对齐"""
        import inspect
        from cloaked_playwright.sync_api import cloaked_sync
        sig = inspect.signature(cloaked_sync)
        params = list(sig.parameters.keys())
        # 应该包含url和proxy
        assert 'url' in params
        assert 'proxy' in params or any('proxy' in str(p) for p in sig.parameters.values())

    def test_return_type_interface(self):
        """验证返回对象接口 — invisible_playwright返回的对象有close/snapshot方法"""
        from cloaked_playwright.sync_api import CloakedBrowser
        expected = {'snapshot', 'close', '__enter__', '__exit__'}
        actual = {m for m in dir(CloakedBrowser) if not m.startswith('_') or m in expected}
        for method in expected:
            assert method in dir(CloakedBrowser), f"Missing method: {method}"
