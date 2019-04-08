#!/usr/bin/env python

from __future__ import absolute_import, unicode_literals

import io

from draftail import (
    __author__,
    __author_email__,
    __copyright__,
    __description__,
    __license__,
    __name__,
    __url__,
    __version__,
)

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with io.open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name=__name__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    copyright=__copyright__,
    packages=find_packages(),
    include_package_data=True,
    keywords=[
        "django",
        "draftail",
        "draftjs",
        "wysiwyg",
        "editor",
        "richtext",
        "markdown",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Editors :: Word Processors",
    ],
    install_requires=["Django>=2.0"],
    extras_require={
        # Keep this in sync with the dependencies in tox.ini.
        "docs": [],
        "testing": [
            # Required for running the tests.
            "tox>=2.3.1",
            # Benchmark dependencies.
            "markov_draftjs==0.1.1",
            "memory-profiler==0.47",
            "psutil==5.4.1",
            # For coverage and PEP8 linting.
            "coverage>=4.1.0",
            "flake8>=3.2.0",
            "isort==4.2.5",
            "black==19.3b0",
        ],
    },
    zip_safe=False,
)
