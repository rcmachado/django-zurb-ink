#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import zurb_ink

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = zurb_ink.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-zurb-ink',
    version=version,
    description="""Django app for Ink responsive email framework""",
    long_description=readme + '\n\n' + history,
    author='Rodrigo Machado',
    author_email='rcmachado@gmail.com',
    url='https://github.com/rcmachado/django-zurb-ink',
    packages=[
        'zurb_ink',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-zurb-ink',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
