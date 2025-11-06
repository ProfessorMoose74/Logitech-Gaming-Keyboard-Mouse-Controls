#!/usr/bin/env python3
"""Setup script for LogiLight"""

from setuptools import setup, find_packages
import os

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="logilight",
    version="1.0.0",
    author="Helyxium Team",
    author_email="dev@helyxium.com",
    description="Easy RGB lighting control for Logitech gaming peripherals on Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ProfessorMoose74/LogiLight",
    project_urls={
        "Bug Tracker": "https://github.com/ProfessorMoose74/LogiLight/issues",
        "Documentation": "https://github.com/ProfessorMoose74/LogiLight#readme",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "click>=8.1.0",
        "rich>=13.0.0",
        "pyyaml>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "logilight=logilight.cli:main",
        ],
    },
)
