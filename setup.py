#!/usr/bin/env python

import io

from setuptools import find_packages, setup

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
        "Programming Language :: Python :: 3",
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
    install_requires=["django>=2.2,<3.0", "draftjs_exporter>=3.0.0,<4.0.0"],
    extras_require={
        "dev": [
            "gunicorn==20.0.4",
            # Code quality.
            "black==19.3b0",
            "isort==4.2.5",
            "flake8==3.7.8",
            "jinjalint>=0.5",
            # Benchmarking.
            "psutil==5.4.1",
            "memory-profiler==0.47",
            "markov_draftjs==0.1.1",
            # Testing.
            "coverage==5.0.3",
            "coveralls==1.11.1",
            "pytest==5.4.1",
            "pytest-django==3.8.0",
        ]
    },
    zip_safe=False,
)
