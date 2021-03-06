#!/usr/bin/env python

from setuptools import setup, find_packages

__AUTHOR__ = 'QuantStack dev team'

setup(
    name='py2vega',
    version='0.6.0',
    description='A Python to Vega-expression transpiler.',
    author=__AUTHOR__,
    maintainer=__AUTHOR__,
    url='https://github.com/QuantStack/py2vega',
    license='BSD 3-Clause',
    keywords='python vega vega-expression',
    packages=find_packages(exclude=['test']),
    python_requires='>=3.6',
    install_requires=[
        'gast>=0.4.0,<0.5'
    ],
    extras_require={
        'testing': ['pytest', 'flake8'],
    },
    platforms=['any'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
