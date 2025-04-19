# -*- coding: utf-8 -*-

# Copyright (c) 2018-2025 Fumito Hamamura <fumito.ham@gmail.com>

# This library is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 3.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.  If not, see <http://www.gnu.org/licenses/>.

# The source code contains parts copied and modified from Spyder project:
# https://github.com/spyder-ide/spyder-kernels
# See below for the original copyright notice.

# -----------------------------------------------------------------------------
# Copyright (c) 2009- Spyder Kernels Contributors
#
# Licensed under the terms of the MIT License
# (see spymx_kernels/__init__.py for details)
# -----------------------------------------------------------------------------

"""Jupyter Kernels for the Spyder consoles."""

# Standard library imports
import ast
import io
import os

# Third party imports
from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))

with io.open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


def get_version(module='spymx_kernels'):
    """Get version."""
    with open(os.path.join(HERE, module, '_version.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version


REQUIREMENTS = [
    'spyder-kernels>=1.8.1'
]

TEST_REQUIREMENTS = [
    # 'codecov',
    # 'cython',
    # 'dask[distributed]',
    # 'flaky',
    # 'matplotlib',
    # 'mock',
    # 'numpy',
    # 'pandas',
    # 'pytest',
    # 'pytest-cov',
    # 'scipy',
    # 'xarray',
    # 'pillow',
]

setup(
    name='spymx-kernels',
    version=get_version(),
    keywords='modelx spyder jupyter kernel ipython console',
    url='https://github.com/fumitoh/spymx-kernels',
    download_url="https://pypi.org/project/spymx-kernels",
    license='LGPLv3',
    author='Fumito Hamamura',
    author_email="fumito.ham@gmail.com",
    description="Jupyter kernels for Spyder plugin for modelx",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['docs', '*tests']),
    install_requires=REQUIREMENTS,
    extras_require={'test': TEST_REQUIREMENTS},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Jupyter',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Interpreters',
    ]
)
