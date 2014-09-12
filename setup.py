import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "exceptional",
    version = "0.01",
    author="Tim Hopper",
    author_email = "tdhopper@gmail.com",
    description = ("Extract Python stack traces from logs"),
    license = "MIT",
    packages = ['exceptional'],
    long_description = read('README.md'),
    install_requires = [],
    entry_points = {
                        'console_scripts': [
                            'exceptional = exceptional.__main__:main'
                        ]
                    }
)