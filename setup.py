# -*- coding: utf-8 -*-
"""Installer for the symbolic.package package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='symbolic.package',
    version='1.0a1',
    description="symbolic.package",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python',
    author='wesleybl',
    author_email='teste@teste.com',
    url='https://github.com/wesleybl/symbolic.package',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/symbolic.package',
        'Source': 'https://github.com/wesleyby/symbolic.package',
        'Tracker': 'https://github.com/wesleyby/symbolic.package/issues',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['symbolic'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7, >=3.6",
    install_requires=[
        'setuptools',
    ],
)
