#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst", "r") as f:
long_description = f.read()

setup(name='trunofficial',
      version='0.1.0',
      description='Unofficial API to the Truecaller phone number search',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      url='https://www.github.com/ritiek/trunofficial',
      keywords=['truecaller', 'search', 'python', 'unofficial', 'api'],
      license='MIT',
      download_url='https://github.com/ritiek/trunofficial/archive/v0.1.0.tar.gz',
      classifiers=[],
     )
