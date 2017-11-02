#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner Jefferson
# V = 0.2 2017

from setuptools import setup, find_packages

setup(
	name='IC SDN',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'texttable',
    ],
    entry_points='''
        [console_scripts]
        ic=ic_sdn.ic:cli
        sdn=ic_sdn.sdn:cli
    ''',
)
