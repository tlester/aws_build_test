#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='aws_build_test',
    version='0.1.0',
    description="Testing AWS build pipeline",
    long_description=readme + '\n\n' + history,
    author="Tom Lester",
    author_email='tom.lester@randrr.com',
    url='https://github.com/tlester/aws_build_test',
    packages=[
        'aws_build_test',
    ],
    package_dir={'aws_build_test':
                 'aws_build_test'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='aws_build_test',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
