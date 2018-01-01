#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Victor Calderon
# Created      : DATE
# Last Modified: DATE
# Vanderbilt University
from __future__ import (print_function, division, 
                            absolute_import)
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, Path Variables"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
__all__        =["git_root_dir"]
"""
Function that looks at the top GIT folder
"""
# Importing Modules
import os
import sys
import git

## Functions
def git_root_dir(path='./'):
    """
    Determines the path to the main `.git` folder of the project.
    Taken from:
    https://goo.gl/46y9v1

    Parameters
    -----------
    path: string, optional (default = './')
        path to the file within the `.git` repository

    Returns
    -----------
    git_root: string
        path to the main `.git` project repository
    """
    # Creating instance of Git Repo
    git_repo = git.Repo(os.path.abspath(path), search_parent_directories=True)
    # Root path
    git_root = git_repo.git.rev_parse("--show-toplevel")

    return git_root

## Adding path to `sys`
sys.path.insert(0, os.path.realpath(git_root_dir(__file__)))