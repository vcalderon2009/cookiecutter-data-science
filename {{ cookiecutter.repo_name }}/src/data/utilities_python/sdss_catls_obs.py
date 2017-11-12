#! /usr/bin/env python

# Victor Calderon
# May 20th, 2017
# Vanderbilt University
from __future__ import print_function, division, absolute_import
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, sdss_catls_obs"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
__all__        =["catl_sdss_dir","extract_catls","output_sdss_dir",\
                 "sdss_catl_clean","sdss_catl_clean_nmin","catl_keys",\
                 "catl_keys_prop","catl_sdss_merge"]
"""
Useful functions to extract the data of sdss catalogues and clean 
it, along with additional functions.
"""
# Importing Modules
import numpy as num
import os
import pandas as pd

# Extra-modules
from . import file_dir_check as fd
from . import get_path       as gp
from . import pandas_hdf5    as phd

from   collections import Counter

def catl_sdss_dir(catl_kind='data', catl_type='mr', sample_s='19',
    catl_info='members', perf_opt=False, print_filedir=True,
    Program_Msg=fd.Program_Msg(__file__)):
    """
    Extracts the path to the catalogues

    Parameters
    ----------
    catl_kind: string, optional (default = 'data')
        type of catalogue to use
        Options:
            - 'data': catalogues comes from SDSS 'real' catalog
            - 'mocks': catalogue(s) come from SDSS 'mock' catalogues

    catl_type: string, optional (default = 'mr')
        type of catalogue to use. It shows which abundance matching method 
        was used for the CLF when assigning halo masses.
        Options:
            - 'mr'   : Uses r-band abs. luminosities
            - 'mstar': Uses stellar masses

    sample_s: string, optional (default = '19')
        volume-limited sample to use.
        Options:
            - '19': Uses the -19 volume-limited 'Consuelo' sample
            - '20': Uses the -20 volume-limited 'Esmeralda' sample
            - '21': Uses the -21 volume-limited 'Carmen' sample

    catl_info: string, optional (default = 'members')
        option for choosing which kind of catalogues to use
        Options:
            - 'members': member galaxies of group catalogues
            - 'groups' : catalogues with group information

    perf_opt: boolean, optional (default = False)
        option for choosing 'perfect' catalogues
        Options:
            - True: Chooses 'perfect' catalogue(s)
            - False: Chooses 'normal' catalogue(s)

    print_filedir: boolean, optional (default = True)
        option for printint out `filedir` on the screen

    Program_Msg: string, optional
        Message used for showing script messages

    Returns
    ----------
    catl_arr: array-like, shape=(N,)
        numpy array of elements/files matching the 'datatype' type in 
        the directory.
    """
    ## Input Parameters
    # Type of catalogue
    if catl_info=='members':
        catl_info_str = 'member_galaxy_catalogues/'
    elif catl_info=='groups':
        catl_info_str = 'group_galaxy_catalogues/'
    else:
        msg = '{0} Invalid `catl_info ({1})`...Exiting'.format(
            Program_Msg, catl_info)
        raise ValueError(msg)
    # 'Perfect' Option
    if perf_opt:
        if catl_kind == 'data':
            msg = '{0} Invalid `catl_kind ({1})` .... Exiting'.format(
                Program_Msg, catl_kind)
            raise ValueError(msg)
        catl_info_str_mod = 'perfect_{0}'.format(catl_info_str)
    else:
        catl_info_str_mod = catl_info_str
    ## Extracting URL of the files
    filedir  = gp.get_output_path()+'SDSS/'+catl_kind+'/'+catl_type+'/'
    filedir += 'Mr'+sample_s+'/'+catl_info_str_mod
    fd.Path_Folder(filedir)
    if print_filedir:
        print('{0} `filedir`: {1}'.format(Program_Msg, filedir))

    return filedir

def extract_catls(catl_kind='data', catl_type='mr', sample_s='19',
    datatype='.hdf5', catl_info='members', perf_opt=False, 
    return_len=False, print_filedir=True,
    Program_Msg=fd.Program_Msg(__file__)):
    """
    Extract the array of catalogues

    Parameters
    ----------
    catl_kind: string, optional (default = 'data')
        type of catalogue to use
        Options:
            - 'data': catalogues comes from SDSS 'real' catalog
            - 'mocks': catalogue(s) come from SDSS 'mock' catalogues

    catl_type: string, optional (default = 'mr')
        type of catalogue to use. It shows which abundance matching method 
        was used for the CLF when assigning halo masses.
        Options:
            - 'mr'   : Uses r-band abs. luminosities
            - 'mstar': Uses stellar masses

    sample_s: string, optional (default = '19')
        volume-limited sample to use.
        Options:
            - '19': Uses the -19 volume-limited 'Consuelo' sample
            - '20': Uses the -20 volume-limited 'Esmeralda' sample
            - '21': Uses the -21 volume-limited 'Carmen' sample

    datatype: string, optional (default = '.hdf5')
        Data type of the files to be indexed in the folder.

    catl_info: string, optional (default = 'members')
        option for choosing which kind of catalogues to use
        Options:
            - 'members': member galaxies of group catalogues
            - 'groups' : catalogues with group information

    perf_opt: boolean, optional (default = False)
        option for choosing 'perfect' catalogues
        Options:
            - True: Chooses 'perfect' catalogue(s)
            - False: Chooses 'normal' catalogue(s)

    return_len: boolean, optional (default = False)
        option to return the number of elements in the directory

    print_filedir: boolean, optional (default = True)
        option for printint out `filedir` on the screen

    Program_Msg: string, optional
        Message used for showing script messages

    Returns
    ----------
    catl_arr: array-like, shape=(N,)
        numpy array of elements/files matching the 'datatype' type in 
        the directory.
    """
    ## Extracting URL of the files
    filedir = catl_sdss_dir(catl_kind=catl_kind,
                            catl_type=catl_type,
                            sample_s=sample_s,
                            catl_info=catl_info,
                            perf_opt=perf_opt,
                            print_filedir=print_filedir)
    ## Converting to numpy arrays
    catl_arr = num.sort(fd.Index(filedir, datatype))
    if len(catl_arr) ==0:
        msg='{0} `catl_arr` contains 0 entries'.format(Program_Msg)
        raise ValueError(msg)

    if return_len:
        return catl_arr, len(catl_arr)
    else:
        return catl_arr

def output_sdss_dir(catl_kind='data', catl_type='mr', sample_s='19',
    Program_Msg=fd.Program_Msg(__file__)):
    """
    Output for sdss directorry, either for `data` or `mocks`

    Parameters
    ----------
    catl_kind: string, optional (default = 'data')
        type of catalogue to use
        Options:
            - 'data': catalogues comes from SDSS 'real' catalog
            - 'mocks': catalogue(s) come from SDSS 'mock' catalogues
    
    catl_type: string, optional (default = 'mr')
        type of catalogue to use. It shows which abundance matching method 
        was used for the CLF when assigning halo masses.
        Options:
            - 'mr'   : Uses r-band abs. luminosities
            - 'mstar': Uses stellar masses

    sample_s: string, optional (default = '19')
        volume-limited sample to use.
        Options:
            - '19': Uses the -19 volume-limited 'Consuelo' sample
            - '20': Uses the -20 volume-limited 'Esmeralda' sample
            - '21': Uses the -21 volume-limited 'Carmen' sample

    Returns
    ----------
    outdir: string
        path to the output directory
    """
    outdir   = gp.get_plot_path()+'SDSS/'+catl_kind+'/'+catl_type+'/'
    outdir  += 'Mr'+sample_s
    fd.Path_Folder(outdir)
    print('{0} `outdir`: {1}'.format(Program_Msg, outdir))

    return outdir

def sdss_catl_clean(catl_pd, catl_kind, catl_info='members', reindex=True):
    """
    Cleans the catalogue removing `failed` values

    Parameters
    ----------
    catl_pd: pandas DataFrame
        dataset with the catalogue information

    catl_kind: string
        type of catalogue to use
        Options:
            - 'data': catalogues comes from SDSS 'real' catalog
            - 'mocks': catalogue(s) come from SDSS 'mock' catalogues

    catl_info: string, optional (default = 'members')
        option for choosing which kind of catalogues to use
        Options:
            - 'members': member galaxies of group catalogues
            - 'groups' : catalogues with group information

    reindex: boolean, optional (default = True)
        option for re-indexing the catalogue

    Return
    ----------
    catl_pd_clean: pandas DataFrame
        `cleaned` version of `catl_pd`, after having removed `failed` values
    """
    ## Mstar-ssfr `failed` values
    ssfr_fail_arr  = [0, -99, -999]
    mstar_fail_arr = [-1, 0]
    # Getting keys for catalogue
    logssfr_key, logmstar_key = catl_keys_prop(catl_kind=catl_kind,
                                               catl_info=catl_info,
                                               return_type='list')
    # Cleaning catalogue
    if catl_kind=='data':
        catl_pd_clean = catl_pd[~catl_pd[ logssfr_key].isin(ssfr_fail_arr) &\
                                 ~catl_pd[logmstar_key].isin(mstar_fail_arr)]
    elif catl_kind=='mocks':
        catl_pd_clean = catl_pd[~catl_pd[ logssfr_key].isin(ssfr_fail_arr)]
    ## Re-indexing
    if reindex:
        catl_pd_clean.reset_index(inplace=True, drop=True)

    return catl_pd_clean

def sdss_catl_clean_nmin(catl_pd, catl_kind, catl_info='members', nmin=1,
    perf_opt=False, Program_Msg=fd.Program_Msg(__file__)):
    """
    Cleans the data and includes only galaxies of a certain `nmin' or 
    higher

    Parameters
    ----------
    catl_pd: pandas DataFrame
        dataset with the catalogue information

    catl_kind: string
        type of catalogue to use
        Options:
            - 'data' : catalogues come from SDSS 'real' catalog
            - 'mocks': catalogue(s) come from SDSS 'mock' catalogues

    catl_info: string, optional (default = 'members')
        option for choosing which kind of catalogues to use
        Options:
            - 'members': member galaxies of group catalogues
            - 'groups' : catalogues with group information

    nmin: integer, optional (default = 1)
        minimum group richness to have in the (galaxy) group catalogue

    perf_opt: boolean, optional (default = False)
        option for using a `perfect` mock catalogue

    Returns
    ----------
    catl_pd_clean: pandas DataFrame
        `cleaned` version of `catl_pd`, after having removed `failed` 
        values and having chosing only galaxies within groups with a
        group richness >= `nmin`
    """
    # Constants
    Cens = int(1)
    Sats = int(0)
    ## Nmin
    try:
        nmin = int(nmin)
    except:
        msg = '{0} Invalid `nmin ({1})` input ... Exiting'.format(
            Program_Msg, nmin)
        raise ValueError(msg)
    # Getting keys for catalogue
    gm_key, id_key, galtype_key = catl_keys(catl_kind, return_type='list',
        perf_opt=perf_opt)
    # Cleaning catalogue
    catl_pd_cl_all = sdss_catl_clean(catl_pd,
                                     catl_kind=catl_kind,
                                     catl_info=catl_info,
                                     reindex=True)
    # Choosing only galaxies in groups of richness >= `nmin`
    if catl_info=='members':
        catl_pd_cens = catl_pd_cl_all.loc[(catl_pd_cl_all[galtype_key]==Cens),id_key]
        catl_pd_cl   = catl_pd_cl_all[(catl_pd_cl_all[id_key].isin(catl_pd_cens))]
        # Group Counts
        group_counts = Counter(catl_pd_cl[id_key])
        group_ngals  = num.array([xx for xx in group_counts.keys() if \
                                  group_counts[xx] >= nmin])
        catl_pd_clean = catl_pd_cl[catl_pd_cl[id_key].isin(group_ngals)]
        catl_pd_clean.reset_index(inplace=True, drop=True)
    elif catl_info=='groups':
        if ('ngals' in catl_pd_cl_all.columns.tolist()):
            catl_pd_clean = catl_pd_cl_all.loc[catl_pd_cl_all['ngals']>=nmin]
            catl_pd_clean.reset_index(inplace=True, drop=True)
        else:
            msg = '{0} Key `ngals` not found in DataFrame ... Exiting'.format(
                Program_Msg)
            raise ValueError(msg)

    return catl_pd_clean

def catl_keys(catl_kind, perf_opt=False, return_type='list'):
    """
    Dictionary keys for the different types of catalogues

    Parameters
    ----------
    catl_kind: string, optional (default = 'data')
        type of catalogue to use
        Options:
            - 'data': catalogues comes from SDSS 'real' catalog
            - 'mocks': catalogue(s) come from SDSS 'mock' catalogues

    perf_opt: boolean, optional (default = False)
        option for using a `perfect` mock catalogue

    return_type: string, optional (default = 'list')
        Type of output to be returned
        Options:
            - 'list': Returns the values as part of a list
            - 'dict': Returns the values as part of a python dictionary

    Returns
    ----------
    catl_keys: python dictionary
        dictionary with the proper keys for the catalogue(s)
        Order: 1) `gm_key`, 2) `id_key`, 3) galtype_key
    """
    ## Perfect catalogue
    if catl_kind=='data':
        perf_opt = False

    ## Property keys
    if catl_kind=='data':
        gm_key      = 'M_h'
        id_key      = 'groupid'
        galtype_key = 'galtype'
    elif catl_kind=='mocks':
        if perf_opt:
            gm_key      = 'M_h'
            id_key      = 'haloid'
            galtype_key = 'galtype'
        else:
            gm_key      = 'M_group'
            id_key      = 'groupid'
            galtype_key = 'g_galtype'
    # Saving values 
    if return_type=='dict':
        catl_dict = {'gm_key':gm_key,'id_key':id_key,'galtype_key':galtype_key}
    elif return_type=='list':
        catl_dict=[gm_key, id_key, galtype_key]

    return catl_dict

def catl_keys_prop(catl_kind, catl_info='members', return_type='list',
    Program_Msg=fd.Program_Msg(__file__)):
    """
    Dictionary key sfor the different galaxy/group properties of 
    catalogues

    Parameters
    ----------
    catl_kind: string, optional (default = 'data')
        type of catalogue to use
        Options:
            - 'data': catalogues comes from SDSS 'real' catalog
            - 'mocks': catalogue(s) come from SDSS 'mock' catalogues

    return_type: string, optional (default = 'list')
        Type of output to be returned
        Options:
            - 'list': Returns the values as part of a list
            - 'dict': Returns the values as part of a python dictionary

    catl_info: string, optional (default = 'members')
        option for choosing which kind of catalogues to use
        Options:
            - 'members': member galaxies of group catalogues
            - 'groups' : catalogues with group information

    Returns
    ----------
    catl_dict: python dictionary
        dictionary with the proper keys for the catalogue(s).
        Order: 1) ssfr_key, 2) mstar_key
    """
    if catl_kind=='data':
        if catl_info=='members':
            logssfr_key  = 'logssfr'
            logmstar_key = 'logMstar_JHU'
        elif catl_info=='groups':
            logssfr_key  = 'logssfr_tot'
            logmstar_key = 'logMstar_tot'
        else:
            msg = '{0} Invalid `catl_info ({1})` ... Exiting'.format(
                Program_Msg, catl_info)
            raise ValueError(msg)
    elif catl_kind=='mocks':
        if catl_info=='members':
            logssfr_key = 'logssfr'
            logmstar_key = 'logMstar'
        elif catl_info == 'groups':
            logssfr_key = 'logssfr'
            logmstar_key = 'logMstar'
        else:
            msg = '{0} Invalid `catl_info ({1})` ... Exiting'.format(
                Program_Msg, catl_info)
    else:
        msg = '{0} Invalid `catl_kind ({1}) ... Exiting'.format(
            Program_Msg, catl_kind)
        raise ValueError(msg)
    # Saving values 
    if return_type=='dict':
        catl_dict = {'logssfr_key':logssfr_key,'logmstar_key':logmstar_key}
    elif return_type=='list':
        catl_dict=[logssfr_key, logmstar_key]

    return catl_dict

def catl_sdss_merge(catl_pd_ii, catl_kind='data', catl_type='mr', sample_s='19',
    perf_opt=False, return_memb_group=False, print_filedir=False,
    Program_Msg=fd.Program_Msg(__file__)):
    """
    Merges the member and group catalogues for a given, and returns 
    a modified version of the galaxy group catalogues with 
    added info about the groups

    Parameters
    ----------
    catl_pd_ii: integers
        index of the catalogue to match, from `extract_catls` function.

    catl_kind: string, optional (default = 'data')
        type of catalogue to use
        Options:
            - 'data': catalogues comes from SDSS 'real' catalog
            - 'mocks': catalogue(s) come from SDSS 'mock' catalogues

    catl_type: string, optional (default = 'mr')
        type of catalogue to use. It shows which abundance matching method 
        was used for the CLF when assigning halo masses.
        Options:
            - 'mr'   : Uses r-band abs. luminosities
            - 'mstar': Uses stellar masses

    sample_s: string, optional (default = '19')
        volume-limited sample to use.
        Options:
            - '19': Uses the -19 volume-limited 'Consuelo' sample
            - '20': Uses the -20 volume-limited 'Esmeralda' sample
            - '21': Uses the -21 volume-limited 'Carmen' sample

    perf_opt: boolean, optional (default = False)
        option for choosing 'perfect' catalogues
        Options:
            - True: Chooses 'perfect' catalogue(s)
            - False: Chooses 'normal' catalogue(s)

    return_memb_group: boolean, optional (default = False)
        option for returning the member and group catalogues, along 
        with the merged catalogue
        If `True': returns merged_pd, memb_pd, group_pd

    print_filedir: boolean, optional (default = True)
        option for printint out `filedir` on the screen

    Program_Msg: string, optional
        Message used for showing script messages

    Returns
    ----------
    catl_pd: pandas DataFrame
        value-added DataFrame with galaxy and group information
    """
    try:
        catl_pd_ii = int(catl_pd_ii)
    except:
        msg = '{0} Invalid `catl_pd_ii ({1}) ... Exiting'.format(
            Program_Msg, catl_pd_ii)
        raise ValueError(msg)
    # Types of catalogues
    catl_info_arr = ['members', 'groups']
    # Extracting Catalogues
    memb_arr, memb_len = extract_catls( catl_kind=catl_kind,
                                catl_type=catl_type,
                                sample_s=sample_s,
                                perf_opt=perf_opt,
                                catl_info=catl_info_arr[0],
                                return_len=True,
                                print_filedir=print_filedir)
    if catl_pd_ii > (memb_len-1):
        msg = '{0} `catl_pd_ii ({1})` out of range ({2})...Exiting'.format(
            Program_Msg, catl_pd_ii, memb_len)
        raise ValueError(msg)
    ## Extracting group and member catalogues
    memb_path  = memb_arr[catl_pd_ii]
    group_path = catl_sdss_dir( catl_kind=catl_kind,
                                catl_type=catl_type,
                                sample_s=sample_s,
                                perf_opt=perf_opt,
                                catl_info=catl_info_arr[1],
                                print_filedir=print_filedir)
    if catl_kind=='mocks':
        group_path += os.path.basename(memb_path).replace('memb', 'group')
    elif catl_kind=='data':
        group_path += os.path.basename(memb_path).replace('Gals', 'Group')
    fd.File_Exists(group_path)
    ## Pandas DataFrames
    memb_pd  = phd.read_hdf5_file_to_pandas_DF(memb_path )
    group_pd = phd.read_hdf5_file_to_pandas_DF(group_path)
    ## Getting Keys for type of catalogue
    gm_key, id_key, galtype_key   = catl_keys(catl_kind,
                                            return_type='list')
    ## Matching keys from Group Catalogue
    if len(num.unique(memb_pd[id_key])) == len(num.unique(group_pd[id_key])):
        group_colnames = num.sort(group_pd.columns)
        group_groupid  = num.sort(num.unique(group_pd[id_key]))
        n_groups       = len(group_groupid)
        n_memb         = len(memb_pd)
        # Initializing column
        # for colname in group_colnames:
        #     print('Initializing colname: {0}'.format(colname))
        #     memb_pd['GG_'+colname] = num.zeros(len(memb_pd))
        # Populating arrays
        # Sorting `memb_pd` by `id_key`
        memb_pd.sort_values(by=id_key, inplace=True)
        memb_pd.reset_index(inplace=True, drop=True)
        group_pd.sort_values(by=id_key, inplace=True)
        group_pd.reset_index(inplace=True, drop=True)
        ## Renaming Columns
        g_colnames_dict = {ii:'GG_'+ii for ii in group_colnames}
        group_pd.rename(columns=g_colnames_dict, inplace=True)
        group_pd.rename(columns={'GG_'+id_key:id_key}, inplace=True)
        ## Merging the two dataframes
        memb_group_pd = pd.merge(left=memb_pd,
                                 right=group_pd,
                                 how='left',
                                 left_on=id_key,
                                 right_on=id_key)
    else:
        msg = '{0} Lenghts of two DataFrames do not match ... Exiting'.format(
            Program_Msg)
        raise ValueError(msg)

    if return_memb_group:
        return memb_group_pd, memb_pd, group_pd
    else:
        return memb_group_pd
