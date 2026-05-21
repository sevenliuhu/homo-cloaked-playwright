# Copyright (c) 2026 HOMO AI. Proprietary. License required. Contact: 16208204@qq.com
from setuptools import setup, find_packages

setup(
    name="cloaked-playwright",
    version="0.1.0",
    description="Chromium stealth browser — Playwright-compatible, powered by CloakBrowser",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Cloaked Dev",
    author_email="dev@cloaked.dev",
    url="https://github.com/sevenliuhu/cloaked-playwright",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        "aiohttp>=3.9",  # 异步API可选
    ],
    extras_require={
        "async": ["aiohttp>=3.9"],
        "dev": ["pytest", "pytest-asyncio"],
    },
    entry_points={
        "console_scripts": [
            "cloaked-playwright=cloaked_playwright.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
    ],
    license="AGPL-3.0",
    project_urls={
        "Source": "https://github.com/sevenliuhu/cloaked-playwright",
        "Bug Reports": "https://github.com/sevenliuhu/cloaked-playwright/issues",
        "Documentation": "https://github.com/sevenliuhu/cloaked-playwright#readme",
    },
)
