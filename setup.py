from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
from glob import glob
from os import path
from os import getenv
from dotenv import load_dotenv

load_dotenv()

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(path.dirname(path.abspath(__file__)),
                    "requirements.txt")) as requirement_file:
    install_requirements = requirement_file.read().split("/n")

name = 'flydenity'
version = getenv('VERSION')
release = version

setup(
    name=name,
    version=version,
    release=release,
    description="Flydenity is an aircraft callsign identification library. Parsers aircraft registration prefix to identify nation of origin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Collen-Roller/arp",
    author='Collen Roller',
    author_email='collen.roller@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['aircraft', 'planes', 'registration', 'callsign', 'prefix',
    'aircraft callsign', 'plane', 'air'],

    packages=find_packages(),

    python_requires='>=3.6', # Version of Python required to install

    install_requires=install_requirements, # Install requirements

    extras_require={
        "dev": ['check-manifest']
    },

    entry_points={
        'console_scripts': [
            'flydenity = flydenity.__main__:main'
        ]
    },
    include_package_data=True # Including package data (IMPORTANT)
)
