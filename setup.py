from setuptools import setup, find_packages

setup(
    name='word-finder',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'fuzzywuzzy',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'word-finder=word_finder.word_finder:main',
        ],
    },
)
