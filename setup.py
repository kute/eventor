#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import dirname, join
from setuptools import setup, find_packages


with open(join(dirname(__file__), 'eventor/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

required = [
    "gevent>=1.1.2",
    "greenlet>=0.4.10",
    "attrs>=16.2.0"
]

setup(
    name='eventor',
    version=version,
    description='Simple API for multi thread or process or Coroutine executor for tasks.',
    long_description=open('README.md', encoding='utf-8').read(),
    author='kute',
    author_email='kutekute00@gmail.com',
    url='https://github.com/kute/eventor',
    packages=find_packages(),
    install_requires=required,
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ),
)
