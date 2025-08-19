#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="selfies-psmiles",            # ★ 원본과 공존을 위해 배포명 변경
    version="0.1.0",                   # ★ 당신 버전으로 갱신
    author="Younggyu Kim",
    author_email="yyy2507@naver.com",
    description="Unofficial extension of SELFIES adding PSMILES '*' endpoint support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KikETs/selfies-psmiles",
    project_urls={
        "Source": "https://github.com/KikETs/selfies-psmiles",
        "Tracker": "https://github.com/KikETs/selfies-psmiles/issues",
    },
    packages=find_packages(exclude=("tests", "docs", "examples")),
    include_package_data=True,
    license="Apache-2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    python_requires=">=3.8",

    # ↓↓↓ 선택 1: 래퍼 방식(업스트림 selfies에 의존) → 주석 해제
    # install_requires=["selfies>=2.2.0"],

    # ↓↓↓ 선택 2: 완전 포크(의존 없음) → 위 줄은 주석 유지
)
