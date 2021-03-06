#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)


def get_long_description():
    """
    Return the README.
    """
    with open("README.md", encoding="utf8") as f:
        return f.read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


setup(
    name="starlette",
    python_requires="~=3.5",
    version=get_version("starlette"),
    url="https://github.com/encode/starlette",
    license="BSD",
    description="The little ASGI library that shines.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Tom Christie",
    author_email="tom@tomchristie.com",
    install_requires=["async_generator"],
    packages=get_packages("starlette"),
    package_data={"starlette": ["py.typed"]},
    include_package_data=True,
    extras_require={
        "full": [
            "aiofiles",
            "graphene",
            "itsdangerous",
            "jinja2",
            "python-multipart",
            "pyyaml",
            "requests",
            "ujson",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    zip_safe=False,
)
