import os
import sys
from setuptools import setup, find_packages

VERSION = "1.0"

setup(
    name="correlation",
    version=VERSION,
    description="",
    author="Thomas Bolden",
    url="https://github.com/ThomasBolden/correlation",
    packages=find_packages,
    install_requires=[
        'matplotlib>=1.5.3', # 2.0.0 ?
        'setuptools>=18.2',  # 19.6 ?
        'numpy>=1.10.4',
        'pandas>=0.22.0',
    ]
)
