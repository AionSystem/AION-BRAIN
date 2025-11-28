"""
Oracle Layer v2.1 Package Setup
"""

from setuptools import setup, find_packages

with open("../README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="oracle-layer",
    version="2.1.0",
    author="Sheldon K. Salmon",
    author_email="AIONSYSTEM@outlook.com",
    description="Embedded Intelligence Protocol - Makes ANY AI self-correct and self-verify",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AIONSYSTEM/AION-BRAIN",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[],
    extras_require={
        "openai": ["openai>=1.0.0"],
        "anthropic": ["anthropic>=0.18.0"],
        "google": ["google-generativeai>=0.3.0"],
        "all": [
            "openai>=1.0.0",
            "anthropic>=0.18.0",
            "google-generativeai>=0.3.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
        ],
    },
    keywords=[
        "ai", "llm", "safety", "verification", "prompt-engineering",
        "openai", "anthropic", "claude", "gpt", "cognitive-architecture"
    ],
    project_urls={
        "Bug Reports": "https://github.com/AIONSYSTEM/AION-BRAIN/issues",
        "Documentation": "https://github.com/AIONSYSTEM/AION-BRAIN",
        "Source": "https://github.com/AIONSYSTEM/AION-BRAIN",
    },
)
