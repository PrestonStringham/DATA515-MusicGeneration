"""
This is the setup.py file for EasyMusicGenerator.
See the README.md file in the root of this repo
for instruction to install this module.
"""

from setuptools import setup, find_packages

setup(
    name='EasyMusicGenerator',
    version='0.1.0',
    packages=find_packages(include=['EasyMusicGenerator',
                                    'EasyMusicGenerator.*']),
    install_requires=[
        'matplotlib==3.3.4',
        'numpy==1.19.5',
        'music21==6.7.0',
    ]
)
