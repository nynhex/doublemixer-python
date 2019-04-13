#!/usr/bin/env python

from setuptools import setup

VERSION = None
with open('doublemixer/__init__.py') as f:
    for line in f:
        if line.startswith('__version__'):
            VERSION = line.replace("'", '').split('=')[1].strip()
            break
if VERSION is None:
    raise ValueError('__version__ not found in __init__.py')

DOWNLOAD_URL = 'https://github.com/teran-mckinney/doublemixer-python/tarball/{}'

DESCRIPTION = 'Bitcoin double mixer CLI and library'

setup(
    python_requires='>=3.3',
    name='doublemixer',
    version=VERSION,
    author='Teran McKinney',
    author_email='sega01@go-beyond.org',
    description=DESCRIPTION,
    keywords=['bitcoin', 'mixer', 'mixing'],
    license='Unlicense',
    url='https://github.com/teran-mckinney/doublemixer-python',
    download_url=DOWNLOAD_URL.format(VERSION),
    packages=['doublemixer'],
    install_requires=[
        'aaargh',
        'bitmix',
        'privcoin'
    ],
    entry_points={
        'console_scripts': [
            'doublemixer = doublemixer:main'
        ]
    }
)
