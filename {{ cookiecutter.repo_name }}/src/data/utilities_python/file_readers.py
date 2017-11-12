#! /usr/bin/env python

# Victor Calderon
# February 16, 2016
# Vanderbilt University

"""
Set of functions to read various types of files
"""
from __future__ import absolute_import
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, file_readers"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
__all__        =["IDL_Read_file","fast_food_reader"]

import sys
import struct
import numpy as num
from scipy.io.idl import readsav
from . import file_dir_check as fd

def IDL_Read_file(filename):
    """
    Reads IDL file as Python dictionary

    Parameters
    ----------
    filename: string
        Absolute path + filename of IDL file being read.

    Returns
    -------
    IDL_dict: python dictionary structure
        Python dictionary that contains the data from IDL `filename`.
    """
    fd.File_Exists(filename)
    try:
        IDL_dict = readsav(filename, python_dict=True)
    except Exception:
        raise Exception ("'{0}' is not an IDL file.".format(filename))

    return IDL_dict

def fast_food_reader(key, nitems, file):
    """ Extracts the data from a binary `FastFood' (.ff) `file`.

    key: string
        type of the element(s) to extract
        Possible values: 'int', 'float', 'double', and 'long'.

    nitems: int
        number of items of type `type_str' to extract.

    file: string
        path of the file, from which to extract the information

    Returns
    -------
    val_arr: array_like
        numpy.array of len(`nitems')        
    """
    Size_types  = { 'int'       :4  , 'float'       :4   , 'char'    :1 ,\
                    'short_int' :2  , 'long_int'    :4   , 'bool'    :1 ,\
                    'double'    :8  , 'long_double' :8   , 'wchart_t':2 }
    
    Type_string = { 'char'         :'c', 'signed_char'       :'b',\
                    'unsigned_char':'B', '_Bool'             :'?',\
                    'short'        :'h', 'unsigned_short'    :'H',\
                    'int'          :'i', 'unsigned_int'      :'I',\
                    'long'         :'l', 'unsigned_long'     :'L',\
                    'long_long'    :'q', 'unsigned_long_long':'Q',\
                    'float'        :'f', 'double'            :'d' }
    errno = 0
    # Defining types and sizes
    if key == 'int':
        size_type = Size_types ['int']
        type_str  = Type_string['int']
    if key == 'float':
        size_type = Size_types ['float']
        type_str  = Type_string['float']
    if key == 'long':
        size_type = Size_types ['long_double']
        type_str  = Type_string['long']
    if key == 'double':
        size_type = Size_types ['double']
        type_str  = Type_string['double']

    # Top Padding (it should contain 4 bytes for .ff files
    # 1st padding = nbyte1
    nbyte1_read = file.read(1*Size_types['int'] )
    nbyte1      = struct.unpack(1*Type_string['int'], nbyte1_read)
    nbyte1_val  = int(nbyte1[0])
    if len(nbyte1) != 1:
        errno = -10
        raise ValueError ('Read error: file empty?. \nError: '+str(errno))
        sys.exit()
    # Extracting data
    nitem1_read = file.read(size_type*nitems)
    val_arr     = struct.unpack( type_str*nitems, nitem1_read)
    val_len     = len(val_arr)
    if val_len != nitems:
        errno = -20
        raise ValueError('Read Error: {0} items expected. Read {1}'.format(
            nitems, val_len))
        sys.exit()
    # Bottom padding
    nbyte2_read = file.read(Size_types['int'])
    nbyte2      = struct.unpack(1*Type_string['int'], nbyte2_read)
    nbyte2_val  = int(nbyte2[0])
    if len(nbyte2)!=1:
        errno = -30
        raise ValueError('Read Error: File too short?\n Errno: '+str(errno))
        sys.exit()
    # Checking top and bottom
    if nbyte1_val != nbyte2_val:
        errno = -1
        Err_msg = 'Read Warning. Byte numbers do not match \n '
        Err_msg += 'nbyte1 = {0}, nbyte2 = {1}\n'.format(nbyte1, nbyte2)
        raise ValueError(Err_msg + 'Errno: {0}'.format(errno))
        sys.exit()
    # Checking that nbye1_val = nitems*Size_type[key]
    if nbyte1_val != nitems*size_type:
        errno = -2
        Err_msg = 'Read Warning. Byte numbers do not match \n '
        Err_msg += 'nbyte1 = {0}, nitems = {1}\n'.format(nbyte1, nitems)
        raise ValueError(Err_msg + 'Errno: {0}'.format(errno))
        sys.exit()
    
    return num.array(val_arr)
