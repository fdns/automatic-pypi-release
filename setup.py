# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import versioneer

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="automatic-pypi-release",
    version=versioneer.get_version(),
    description="A pip package",
    license="MIT",
    author="Felipe Espinoza",
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
