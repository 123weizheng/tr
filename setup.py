#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import os

import tools

_BASEDIR = os.path.dirname(os.path.abspath(__file__))
for big_file in tools.BIG_FILES:
    tools.join(os.path.join(_BASEDIR, big_file))

appname = "tr"
version = "1.0.0.5"

with open("README.md", "r") as f:
    readme = f.read()

packages = ["tr", "libtorch"]

setup(
    name=appname,
    version=version,
    description=(
        '''%s''' % appname
    ),

    author='anycode',
    author_email='anycode@yahoo.com',
    maintainer='anycode',
    maintainer_email='anycode@yahoo.com',
    packages=packages,
    platforms=["all"],
    url='https://pypi.org/project/%s/' % appname,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
    ],
    include_package_data=True,

    long_description=readme,
    long_description_content_type='text/markdown'
)