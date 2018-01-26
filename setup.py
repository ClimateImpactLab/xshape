#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pyshp',
    'xarray',
    'numpy',
    'pandas',
    'matplotlib'
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(delgadom): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='xshape',
    version='0.1.1',
    description="Tools for working with shapefiles, topographies, and polygons in xarray",
    long_description=readme + '\n\n' + history,
    author="Michael Delgado",
    author_email='delgado.michaelt@gmail.com',
    url='https://pypi.python.org/pypi',
    packages=find_packages(include=['xshape']),
    entry_points={
        'console_scripts': [
            'xshape=xshape.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='xshape',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
