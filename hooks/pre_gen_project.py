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
    pkg = pkg.decode('utf-8')
    print('>> Checking {0}'.format(pkg))
    ## Installing packages
    try:
        os.system('pip -q install {0}'.format(pkg))
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
    PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
    ##
    ## Reading in list of packages
    reqfile = os.path.join(PROJECT_DIRECTORY, 'requirements.txt')
    if not (os.path.exists(reqfile)):
        msg = '`reqfile` ({0}) was not found!'.format(reqfile)
        raise ValueError(msg)
    ##
    ## Parsing packages needed
    with open(reqfile, 'rb') as req_f:
        req_f_pkgs = req_f.readlines()
        for pkg_ii in req_f_pkgs:
            import_pkgs(pkg_ii)

if __name__=='__main__':
    main()
