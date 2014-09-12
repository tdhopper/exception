import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "exceptional",
    version = "0.01",
    author = "Tim Hopper",
    author_email = "tdhopper@gmail.com",
    description = ("Extract Python stack traces from logs"),
    license = "MIT",
    packages=['exceptional'],
    long_description=read('README.md'),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'exceptional = exceptional.__main__:main'
        ]
    }
)