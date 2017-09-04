#!/usr/bin/env python

from setuptools import setup, find_packages
import trunofficial

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='trunofficial',
      version=trunofficial.__version__,
      description='Unofficial API to the Truecaller phone number search',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'trunofficial = trunofficial.trunofficial:command_line',
            ]
      },
      url='https://www.github.com/ritiek/trunofficial',
      keywords=['truecaller', 'search', 'python', 'unofficial', 'api'],
      license='MIT',
      download_url='https://github.com/ritiek/trunofficial/archive/v' + trunofficial.__version__ + '.tar.gz',
      classifiers=[],
     )
