#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'argparse',
    'six'
]

test_requirements = [
]

setup(
    name='exceptional',
    version='0.1.0',
    description="Extract unique Python exceptions with their traceback from a log file. ",
    long_description=readme + '\n\n' + history,
    author="Timothy Hopper",
    author_email='tdhopper@gmail.com',
    url='https://github.com/tdhopper/exceptional',
    packages=[
        'exceptional',
    ],
    package_dir={'exceptional':
                 'exceptional'},
    entry_points={
        'console_scripts': [
            'exceptional=exceptional.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='exceptional',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
