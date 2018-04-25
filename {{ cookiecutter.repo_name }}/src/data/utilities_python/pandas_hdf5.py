#! /usr/bin/env python

# Victor Calderon
# February 22, 2016
# Vanderbilt University

"""
Tools for converting pandas DataFrames to .hdf5 files, and converting from 
one type of hdf5 file to `pandas_hdf5` file format
"""
from __future__ import print_function, division, absolute_import
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, geometry"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
__all__        =["read_pandas_hdf5","read_hdf5_file_to_pandas_DF",\
                 "pandas_file_to_hdf5_file","hdf5_file_to_pandas_file",\
                 "pandas_df_to_hdf5_file","concadenate_pd_df"]

import numpy as num
import pandas as pd
import h5py
from . import file_dir_check as fd
import os

def read_pandas_hdf5(hdf5_file, key=None, ret=False):
    """
    Reads a `.hdf5` file that contains one or many datasets, and converts into 
    a pandas DataFrame. It assumes that the file is a PyTable

    Parameters
    ----------
    hdf5_file: string
        Path to `.hdf5` file containing one or many pandas DataFrame(s).

    key: string
        If provided, it will extract `key` as a pandas DataFrame

    ret: boolean, (default=False)
        Option to return key of the file. 

    Returns
    -------
    pd_dataframe: pandas DataFrame object
        DataFrame from `hdf5_file` with under the `key` directory.
    """
    Program_Message = fd.Program_Msg(__file__)
    fd.File_Exists(hdf5_file)
    # Checking number of keys
    hdf5_file_obj  = pd.HDFStore(hdf5_file)
    hdf5_file_keys = [key_ii for key_ii in hdf5_file_obj.keys()]
    hdf5_file_obj.close()
    if key==None:
        try:
            pd_dataframe = pd.read_hdf(hdf5_file)
            if ret: return pd_dataframe, hdf5_file_keys[0]
            else: return pd_dataframe
        except:
            print('{0} Must specify which key to use:'.format(Program_Message))
            print('Possible keys: \n')
            for key1, name in enumerate(hdf5_file_keys):
                print('\t Key {0}:   {1}'.format(key1,name))
    else:
        if key not in hdf5_file_keys:
            print('{0} Key not in the file:'.format(Program_Message))
            print('Possible keys: \n')
            for key1, name in enumerate(hdf5_file_keys):
                print('\t Key {0}:   {1}'.format(key1,name))
        else:
            pd_dataframe = pd.read_hdf(hdf5_file, key=key)
            if ret: return pd_dataframe, key
            else: return pd_dataframe

def read_hdf5_file_to_pandas_DF(hdf5_file, key=None):
    """
    Reads content of HDF5 file and converts it to Pandas DataFrame

    Parameters
    ----------
    hdf5_file: string
        Path to HDF5 file with the data

    key: string, default=None
        Key or path in hdf5 file for the pandas DataFrame and the normal hddf5 
        file

    Returns
    -------
    pd_dataframe: Pandas DataFrame
        DataFrame from `hdf5_file` with under the `key` directory.
    """
    Program_Message = fd.Program_Msg(__file__)
    fd.File_Exists(hdf5_file)
    ##
    ## Reading in Pandas DataFrame
    try:
        pd_dataframe = pd.read_hdf(hdf5_file, key=key)
        return pd_dataframe
    except:
        msg = '{0} Could not read `{1}`! Please check if the file is correct'
        msg = msg.format(Program_Message, hdf5_file)
        raise ValueError(msg)

# def read_hdf5_file_to_pandas_DF(hdf5_file, key=None):
#   """
#   Reads content of HDF5 file and converts it to Pandas DataFrame

#   Parameters
#   ----------
#   hdf5_file: string
#       Path to HDF5 file with the data

#   key: string, default=None
#       Key or path in hdf5 file for the pandas DataFrame and the normal hddf5 
#       file

#   Returns
#   -------
#   pd_dataframe: Pandas DataFrame
#       DataFrame from `hdf5_file` with under the `key` directory.
#   """
#   Program_Message = fd.Program_Msg(__file__)
#   fd.File_Exists(hdf5_file)
#   data_file = h5py.File(hdf5_file,'r')
#   pd_dict = {}
#   if not key:
#       data_keys = num.array([key_ii for key_ii in data_file.keys()])
#       if len(data_keys)==1:
#           data = data_file.get(data_keys[0])
#           for name in data.name:
#           # for name in data.dtype.names:
#               name1 = name.replace('-','_')
#               pd_dict[name1] = data[name]
#           pd_dataframe = pd.DataFrame(pd_dict)
#           return pd_dataframe
#       else:
#           print('{0} Must specify which key to use:'.format(Program_Message))
#           print('Possible keys: \n')
#           for key, name in enumerate(data_keys):
#               print('\t Key {0}:   {1}'.format(key,name))
#   else:
#       data_keys = num.array([key_ii for key_ii in data_file.keys()])
#       if key not in data_keys:
#           print('{0} Key not in the file:'.format(Program_Message))
#           print('Possible keys: \n')
#           for key, name in enumerate(data_keys):
#               print('\t Key {0}:   {1}'.format(key,name))
#       else:
#           data = data_file.get(key)
#           for name in data.dtype.names:
#               name1 = name.replace('-','_')
#               pd_dict[name1] = data[name]
#           pd_dataframe = pd.DataFrame(pd_dict)
#           return pd_dataframe
#   data_file.close()

def pandas_file_to_hdf5_file(pandas_hdf5_file, hdf5_file, key=None, mode='w'):
    """
    Reads hdf5 file with pandas structure, and turns it into a normal HDF5 file.

    Parameters
    ----------
    pandas_hdf5_file: string
        Path to the hdf5 file containing pandas DataFrame

    hdf5_file: string
        Path to output hdf5 file containing arrays as keys

    key: string, optional (default: None)
        Key or path in hdf5 file for the pandas DataFrame and the normal hddf5 
        file
    """
    fd.File_Exists(pandas_hdf5_file)
    if not key:
        data, key  = read_pandas_hdf5(pandas_hdf5_file, key=None, ret=True)
    else:
        data  = read_pandas_hdf5(pandas_hdf5_file,key=key)
    arr_names   = data.dtypes.index.values
    dtypes_arr  = data.dtypes.values
    dtypes_arr  = num.array([x.str for x in dtypes_arr])
    data_dtypes = num.dtype(zip(arr_names,dtypes_arr))
    dataset     = num.recarray((len(data),),dtype=data_dtypes)
    for name in dataset.dtype.names:
        dataset[name] = data[name]
    # Saving file
    hdf5_file1 = h5py.File(hdf5_file,mode=mode)
    hdf5_file1.create_dataset(key, data=dataset)
    hdf5_file1.close()
    print('{0}: HDF5 New file-> {1}'.format(fd.Program_Msg(__file__),hdf5_file))

def hdf5_file_to_pandas_file(hdf5_file, pandas_hdf5_file, key=None):
    """
    Reads hdf5 file with pandas structure, and turns it into a normal HDF5 file.

    Parameters
    ----------
    hdf5_file: string
        Path to hdf5 file containing arrays as keys

    pandas_hdf5_file: string
        Path to the output hdf5 file containing pandas DataFrame

    key: string, optional (default: None)
        Key or path in hdf5 file for the pandas DataFrame and the normal hddf5 
        file
    """
    Program_Message = fd.Program_Msg(__file__)
    fd.File_Exists(hdf5_file)
    data_file = h5py.File(hdf5_file,'r')
    pd_dict = {}
    if not key:
        data_keys = num.array([key_ii for key_ii in data_file.keys()])
        if len(data_keys)==1:
            data = data_file.get(data_keys[0])
            for name in data.dtype.names:
                name1 = name.replace('-','_')
                pd_dict[name1] = data[name]
            pd_dataframe = pd.DataFrame(pd_dict)
            pd_file_HDF  = pd.HDFStore(pandas_hdf5_file)
            pd_file_HDF.put(data_keys[0],pd_dataframe, format='table',
                data_columns=True)
            pd_file_HDF.close()
            print('{0} Pandas File: {1}'.format(Program_Message, pandas_hdf5_file))
        else:
            print('{0} Must specify which key to use:'.format(Program_Message))
            print('Possible keys: \n')
            for key, name in enumerate(data_keys):
                print('\t Key {0}:   {1}'.format(key,name))
    else:
        data_keys = num.array([key_ii for key_ii in data_file.keys()])
        if key not in data_keys:
            print('{0} Key not in the file:'.format(Program_Message))
            print('Possible keys: \n')
            for key, name in enumerate(data_keys):
                print('\t Key {0}:   {1}'.format(key,name))
        else:
            data = data_file.get(key)
            for name in data.dtype.names:
                name1 = name.replace('-','_')
                pd_dict[name1] = data[name]
            pd_dataframe = pd.DataFrame(pd_dict)
            pd_file_HDF  = pd.HDFStore(pandas_hdf5_file)
            pd_file_HDF.put(data_keys[0],pd_dataframe, format='table',
                data_columns=True)
            print('{0} Pandas File: {1}'.format(Program_Message, pandas_hdf5_file))
    data_file.close()

def pandas_df_to_hdf5_file(data, hdf5_file, key=None, mode='w',
    complevel=8):
    """
    Saves a pandas DataFrame into a normal or a `pandas` hdf5 file.

    Parameters
    ----------
    data: pandas DataFrame object
        DataFrame with the necessary data

    hdf5_file: string
        Path to output file (HDF5 format)

    key: string
        Location, under which to save the pandas DataFrame

    mode: string, optional (default = 'w')
        mode to handle the file.

    complevel: int, range(0-9), optional (default = 8)
        level of compression for the HDF5 file
    """
    ##
    ## Saving DataFrame to HDF5 file
    try:
        data.to_hdf(hdf5_file, key, mode=mode, complevel=complevel)
        print('{0}: HDF5 New file-> {1}'.format(fd.Program_Msg(__file__),hdf5_file))
    except:
        msg = '{0} Could not create HDF5 file'.format(fd.Program_Msg(__file__))
        raise ValueError(msg)


# def pandas_df_to_hdf5_file(data, hdf5_file, kind='pandas', key=None, mode='w'):
#   """
#   Saves a pandas DataFrame into a normal or a `pandas` hdf5 file.

#   Parameters
#   ----------
#   data: pandas DataFrame object
#       DataFrame with the necessary data

#   hdf5_file: string
#       Path to output file (HDF5 format)

#   kind: string, optional (default='pandas')
#       Option to determine the method to use for saving the DataFrame
#       - 'pandas': Outputs HDF5 file as PyTable 
#       - 'normal': Outputs HDF5 as structured array.

#   key: string
#       Location, under which to save the pandas DataFrame
#   """
#   assert(kind=='pandas' or kind=='normal')
#   if not key:
#       key = '/Main'
#   if kind=='pandas':
#       arr_names   = data.dtypes.index.values
#       dtypes_arr  = data.dtypes.values
#       data_dtypes = num.dtype(zip(arr_names,dtypes_arr))
#       dataset     = num.recarray((len(data),),dtype=data_dtypes)
#       for name in dataset.dtype.names:
#           dataset[name] = data[name]
#       # Saving file
#       hdf5_file1 = h5py.File(hdf5_file, mode=mode)
#       try:
#           hdf5_file1.create_dataset(key, data=dataset,
#               compression="gzip", compression_opts=9)
#       except RuntimeError: 
#           del hdf5_file1[key]
#           hdf5_file1.create_dataset(key, data=dataset,
#               compression="gzip", compression_opts=9)
#       hdf5_file1.close()
#   elif kind=='normal':
#       data_keys    = data.columns.values
#       pd_file_HDF  = pd.HDFStore(hdf5_file)
#       try:
#           pd_file_HDF.put(key, data, format='table', data_columns=True)
#       except:
#           pd_file_HDF.close()
#           pd_file_HDF = h5py.File(hdf5_file)
#           del pd_file_HDF[key]
#           pd_file_HDF.close()
#           pd_file_HDF.put(key, data, format='table', data_columns=True)

#       print('{0}: HDF5 New file-> {1}'.format(fd.Program_Msg(__file__),hdf5_file))
#   else:
#       print('{0} Could not create HDF5 file'.format(fd.Program_Msg(__file__)))

def concadenate_pd_df(direc, file_type='hdf5', foutput=None, outonly=True):
    """
    Concadenates pandas DataFrame into a single DataFrame

    Parameters
    ----------
    direc: string
        path to the folder containing the pandas hdf5 files

    file_type: string, optional (default='hdf5')
        file format of the file in `direc' to be read

    foutput: NoneType or string, optional (default=None)
        if not `None', it is the basename of the output file in `.hdf5' format

    outonly: boolean, optional (default=True)
        option for returning pandas DataFrame.
        If `True', it returns the pandas DataFrame

    Returns
    -------
    df_conc: pandas DataFrame
        DataFrame containing the combined information of files in `direc'
    """
    # Checking existence of folder
    fd.Path_Folder(direc)
    # List of files in `direc'
    df_files = fd.Index(direc, '.{0}'.format(file_type))
    if len(df_files) > 0:
        df_files = num.sort(df_files)
        df_conc  = read_pandas_hdf5(df_files[0])
        print('\n{0} Found {1} files'.format(fd.Program_Msg(__file__), len(df_files)))
        if len(df_files) > 1:
            for ii in range(1, len(df_files)):
                df_conc = pd.concat([df_conc, read_pandas_hdf5(df_files[ii])], 
                    ignore_index=True)
        if (foutput is not None) and (type(foutput)==str):
            foutput_file = '{0}/{1}.{2}'.format(direc, foutput, file_type)
            pandas_df_to_hdf5_file(df_conc, foutput_file, 
                key='/Main')
            fd.File_Exists(foutput_file)
            print('\n\t ==> foutput_file: {0}\n'.format(foutput_file))
        if outonly:
            return df_conc
        else:
            pass
    else:
        raise ValueError("\n\t ===> No files of `.{0}' in `{1}'\n\n".format(
            file_type, direc))


