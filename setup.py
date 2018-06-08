#!/usr/bin/env python3
from setuptools import setup

setup(name='toolbox-cryptography',
      version='0.1',
      author='Fang Han',
      author_email='hanfa@umich.edu',
      packages=['attacktypes', 'utilalgorithms'],
      scripts=['bin/crypto-attack-types', 'bin/crypto-caeser', 'bin/crypto-poly-mult']
      )
