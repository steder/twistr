#!/usr/bin/env python

from setuptools import setup


setup(
    name="Twistr",
    version="2.0.0",
    description="Twistd wrapper that restarts twisted on code changes",
    long_description=open("README.rst", "r").read(),
    author="Mike Steder",
    author_email="steder@gmail.com",
    url="http://github.com/steder/twistr",
    scripts=["bin/twistr"],
    install_requires=["twisted"],
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
