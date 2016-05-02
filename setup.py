#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup


version = '1.0'


setup(
    name='fcn',
    version=version,
    packages=find_packages(),
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/FCN',
    license='MIT',
    keywords='machine learning',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
    ],
)