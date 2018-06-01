#!/usr/bin/env python

import glob
import os

from setuptools import find_packages, setup

# Get some values from the setup.cfg
try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser

conf = ConfigParser()
conf.read(['setup.cfg'])
metadata = dict(conf.items('metadata'))

# Metadata
PACKAGENAME = metadata.get('package_name', 'src')
DESCRIPTION = metadata.get('description', '{{cookiecutter.short_description}}')
AUTHOR = metadata.get('author', '{{cookiecutter.author_name}}')
AUTHOR_EMAIL = metadata.get('author_email', '{{cookiecutter.author_email}}')
LICENSE = metadata.get('license', 'unknown')
VERSION = metadata.get('version', '0.0.0dev')
URL = metadata.get('url', '')

# Long Description
readme_glob = 'README*'
_cfg_long_description = metadata.get('long_description', '')
if _cfg_long_description:
    LONG_DESCRIPTION = _cfg_long_description
elif os.path.exists('LONG_DESCRIPTION.rst'):
    with open('LONG_DESCRIPTION.rst') as f:
        LONG_DESCRIPTION = f.read()
elif len(glob.glob(readme_glob)) > 0:
    with open(glob.glob(readme_glob)[0]) as f:
        LONG_DESCRIPTION = f.read()
else:
    LONG_DESCRIPTION = ''

setup(
    name=PACKAGENAME,
    version=VERSION,
    packages=find_packages(),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL)
