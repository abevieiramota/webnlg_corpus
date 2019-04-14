# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', 'r') as f:

    long_description = f.read()

setup(name='webnlg_corpus',
      version='0.1.dev8',
      url='https://github.com/abevieiramota/webnlg_corpus',
      license='CC BY-NC-SA 4.0',
      author='Abelardo Vieira Mota',
      author_email='abevieiramota@gmail.com',
      description='WebNLG Corpus',
      packages=find_packages(),
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
              'Intended Audience :: Education',
              'Programming Language :: Python :: 3',
              'Topic :: Scientific/Engineering :: Artificial Intelligence'
              ],
      install_requires=[
              'pandas',
              'tinydb'
              ]
      )
