#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

def import_pkgs(pkg):
    """
    Tries to import the necessary packages.

    Parameters
    -----------
    pkg : `str`
        Name of the package to install
    """
    ## Message for `pkg`
    print('>> Checking {0}'.format(pkg))
    ## Installing packages
    try:
        print('pip -q install {0}'.format(pkg))
        # os.system('pip -q install {0}'.format(pkg))
    except:
        msg = '`pkg` ({0}) not found!'.format(pkg)
        raise ValueError(msg)

def main():
    """
    Making sure packages are installed before running cookiecutter.
    """
    ## Pip package
    try:
        import pip
    except ImportError:
        msg = '`pip` must be installed first. Please install this beforehand!'
        raise ImportError(msg)
    ##
    ## Project directory
    PROJECT_DIRECTORY = os.path.relpath(os.path.curdir)
    ##
    ## Reading in list of packages
    reqfile = os.path.join(PROJECT_DIRECTORY, 'requirements.txt')
    if not (os.path.exists(reqfile)):
        msg = '`reqfile` ({0}) was not found!'.format(reqfile)
        raise ValueError(msg)
    ##
    ## Running `install requirements.txt`
    try:
        os.system('pip install -r {0}'.format(reqfile))
    except:
        msg = 'Could not install requirements!!'
        raise ValueError(msg)

if __name__ == '__main__':
    main()
