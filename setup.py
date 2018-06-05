##############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from setuptools import setup, find_packages

setup(
    name="Products.ZMySQLDA",
    version="4.0.dev0",
    license="ZPL 2.1",
    author="HOFFMANN+LIEBENBERG in association with "
            "SNTL Publishing, Andy Dustman, John Eikenberry",
    author_email="zms@sntl-publishing.com",
    url="https://github.com/zms-publishing/Products.ZMySQLDA",
    description="MySQL Zope adapter.",
    long_description="MySQL Database Adapter for Zope.",
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
    ],
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=["Products"],
    zip_safe=False,
    install_requires=[
        "mysqlclient",
        "Zope",
        "Products.ZSQLMethods",
    ]
)