#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'click==2.0',
    'requirements-parser==0.0.6',
    'wheel==0.23.0'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='wheelmaker',
    version='0.1.0',
    description='Creates wheel files from a requirements file',
    long_description=readme + '\n\n' + history,
    author='Franco Mariluis',
    author_email='fmariluis@msa.com.ar',
    url='https://github.com/fmariluis/wheelmaker',
    packages=[
        'wheelmaker',
    ],
    package_dir={'wheelmaker':
                 'wheelmaker'},
    scripts=['wheelmaker/wheelmaker'],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='wheelmaker',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)