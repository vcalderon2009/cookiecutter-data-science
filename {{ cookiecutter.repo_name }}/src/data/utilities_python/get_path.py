#!/usr/bin/env python
'''
Description:
    Setup file paths for systems that I usually work on.
'''

#Duncan Campbell
#September 2, 2012
#Yale University
#Setup file paths for common systems I work on.

from __future__ import absolute_import
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, get_path"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
__all__        =["get_system", "get_base_path", "get_code_c",\
                 "get_output_path", "git_root_dir",
                 "cookiecutter_paths"]

# Importing modules
import git
import os
from . import file_dir_check as fd

def known_systems():
    return ['bender', 'Victors-MacBook-Pro-2']

def get_system():
    """
    get the name of the system
    """
    import os, sys
    path_to_home = os.getenv("HOME")
    
    host = os.popen('echo $HOSTNAME').read()
    host = host.split('.')[0]
    host = host.split('\n')[0]
    
    if host in known_systems(): return host
    else:
        host = None
        if os.path.isfile(os.getenv("HOME")+'/.bender'): host = 'bender'
        elif os.path.isfile(os.getenv("HOME")+'/.victor-mac-pro'): 
            host = 'Victors-MacBook-Pro-2'
        else: raise ValueError('unknown system.')
        return host

def get_base_path(node=None):
    """
    get the base path for the system
    """
    if node==None: node = get_system()
    ##
    ## Base path
    try:
        path = os.environ['sdss_catl_path']
        assert(os.path.exists(path))
    except:
        proj_dict = cookiecutter_paths(__file__)
        ##
        ## Path to `base`
        path = proj_dict['base_dir']

    return path

def get_code_c(node=None):
    """
    get the base path to codes in c for the system
    """
    if node==None: node = get_system()
    if node=='bender': 
        path='/home/caldervf/Codes2/custom_utilities_c/'
    elif node=='Victors-MacBook-Pro-2':
        path='/Users/victor2/Codes/custom_utilities_c/'
    else:
        raise ValueError ('error: unknown code directory for this environment')

    return path

def get_output_path(node=None):
    """
    get the base path to get_output_path storage for the system
    """
    if node==None: node = get_system()

    path = os.path.join(get_base_path(),'data','processed')
    
    return path

## Based on the `Data Science` Cookiecutter Template
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

def cookiecutter_paths(path='./'):
    """
    Paths to main folders in the `Data Science` Cookiecutter template.
    
    Parameters
    -----------
    path: string, optional (default = './')
        path to the file within the `.git` repository

    Returns
    ------------
    param_dict: python dictionary
        dictionary with info of the project that uses the
        `Data Science` Cookiecutter template.
    """
    # Base path
    base_dir = git_root_dir(path) + '/'
    assert(os.path.exists(base_dir))
    # Plot Path
    plot_dir = base_dir + 'reports/figures/'
    fd.Path_Folder(plot_dir)
    # Source Code Path
    src_dir = base_dir + 'src/data/'
    fd.Path_Folder(src_dir)
    # Data Path
    data_dir = base_dir + 'data/'
    fd.Path_Folder(data_dir)
    # Saving into dictionary
    param_dict = {}
    param_dict['base_dir'] = base_dir
    param_dict['plot_dir'] = plot_dir
    param_dict['src_dir' ] = src_dir
    param_dict['data_dir'] = data_dir

    return param_dict
