#!/usr/bin/env python

import codecs
from setuptools import setup
from sphinx_typlog_theme import __version__

with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='sphinx_typlog_theme',
    version=__version__,
    description='A typlog Sphinx theme',
    long_description=readme,
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    url='https://github.com/typlog/sphinx-typlog-theme',
    packages=['sphinx_typlog_theme'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'sphinx_typlog_theme = sphinx_typlog_theme',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
