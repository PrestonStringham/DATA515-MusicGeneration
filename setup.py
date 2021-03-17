"""
This is the setup.py file for EasyMusicGenerator.
See the README.md file in the root of this repo
for instruction to install this module.
"""

from setuptools import setup, find_packages

setup(
    name='EasyMusicGenerator',
    version='0.1.0',
    packages=find_packages(include=['easy_music_generator',
                                    'easy_music_generator.preprocessor',
                                    ]),
    install_requires=[
        'numpy==1.20',
        'scipy',
        'pandas',
        'scikit-learn',
        'matplotlib==3.3.4',
        'seaborn',
        'magenta',
        'music21==6.7.0',
    ]
)
