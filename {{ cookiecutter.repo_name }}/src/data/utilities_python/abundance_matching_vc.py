#! /usr/bin/env python

# Victor Calderon
# February 20, 2016
# Vanderbilt University

"""
Set of functions for abundance matching
"""
from __future__ import division, absolute_import, print_function

__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, abundance_matching_vc"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
__all__        =["abundance_matching_f", "cumulative_function"]

import numpy as num
from   scipy.interpolate import interp1d

def _reversed_arrays(x,y):
	"""
	Determines if arrays increase/decrease monotonically.

	Parameters
	----------
	x: array_like
		numpy.array containing `x` values

	y: array_like
		numpy.array containing elements `y(x)` related to `x`

	Returns
	-------
	rel: boolean
		- rel==True: if `x` increases with increasing `y(x)` monotonically
		- rel==False: if `x` decreases with increasing `y(x)` monotonically
	"""
	x = num.array(x)
	y = num.array(y)

	n_greater = 0.
	n_less    = 0.

	for ii in range(1,len(x)):
		if y[ii]>y[ii-1]: n_greater += 1
		else: n_less += 1

	if (n_greater > n_less):
		return False
	else: return True

def _monotonic_arrays(x,y):
	"""
	Determines if arrays are monotonically increasing or decreasing

	Parameters
	----------
	x: array_like
		numpy.array containing `x` values

	y: array_like
		numpy.array containing elements `y(x)` related to `x`

	Returns
	-------
	rel: boolean
		- rel==True if increasing monotonically
		- rel==False if decreasing monotonically
	"""
	idx_sort = num.argsort(x)[::1]
	x = x[idx_sort]
	y = y[idx_sort]

	n_greater = 0.
	n_less    = 0.

	for ii in range(1,len(x)):
		if y[ii] > y[ii-1]: n_greater += 1.
		else: n_less += 1.

	if (n_greater==len(x)-1) | (n_less==len(x)-1):
		return True
	else: return False

def abundance_matching_f(dict1, dict2, volume1=1., volume2=1., 
    reverse=True, dens1_opt=False):
    """
    Does abundance matching based on two quantities (dict1 and dict2).
    It assigs values from `dict2` to elements in `dict1`.

    Parameters
    ----------
    dict1: dictionary_like, or array_like
        Dictionary of property 1
        - Keys: `var`: First variable to be analyzed
                `dens`: Density array corresponding to `var` elements.
                        Given if dens1==True

    dict2: dictionary_like, or array_like
        Dictionary of property 2
        - Keys: `var`: First variable to be analyzed
                `dens`: Density array corresponding to `var` elements.
                        Given if dens1==True

    volume1: float
        volume corresponding to dict1

    reverse: boolean
        Determines the relation between var1 and var2.
        - reverse==True: var1 increases with increasing var2
        - reverse==False: var1 decreases with increasing var2

    dens1_opt: boolean, default=False
        - If 'True': density is already provided as key for `dict1`
        - If 'False': density must me calculated

    Returns
    -------
    var1_ab: array_like
        numpy.array of elements matching those of `dict1`, after matching with 
        dict2.
    """
    # 2nd Property
    var2  = num.array(dict2['var' ])
    dens2 = num.array(dict2['dens'])
    if dens1_opt==True:
        # 1st Property
        var1  = num.array(dict1['var' ])
        dens1_1 = num.array(dict1['dens'])
    elif dens1_opt==False:
        # 1st Property
        var1  = dict1.copy()
        if reverse:
        # if _reversed_arrays(var2,dens2):
            dens1 = num.array([num.where(var1<xx)[0].size for xx in var1])+1
        else:
            dens1 = num.array([num.where(var1>xx)[0].size for xx in var1])+1
        dens1 = dens1.astype(float)/volume1
    else:
        raise AssertionError ('Assertion_Error')
    # Interpolation
    interp_var2 = interp1d(dens2,var2,bounds_error=True,assume_sorted=False)
    # Assignment
    var1_ab = num.array([interp_var2(xx) for xx in dens1])

    return var1_ab

def cumulative_function(var,volume=1.,reverse=True, dens=True):
    """
    Computes the cumulative function y(var) for var

    Parameters
    ----------
    var: array_like
        variable to be analyzed

    volume: float
        volume of the survey. Used to calculate densities

    reverse: boolean, (default=True)
        Determines the relation of var and density
        - reverse==True : as var increases, dens decreases
        - reverse==False: as var increases, dens increases

    dens: boolean, (default=True)
        Option to return counts or densities
        - dens==True: Return densities
        - dens==False: Return actual counts

     Returns
     -------
     y_x: array_like
        Cumulative function of number counts or densities, depending of `dens`
    """
    var = num.array(var)
    if reverse:
        counts = num.array([num.where(var<x)[0].size for x in var])+1
    else:
        counts = num.array([num.where(var>x)[0].size for x in var])+1
    if dens:
        counts = counts.astype(float)/volume

    return counts

