#! /usr/bin/env python

# Victor Calderon
# February 15, 2016
# Vanderbilt University

"""
Set of statistics tools used in my codes
"""
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, statistics_vc"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
__all__        =["myceil","myfloor","Bootstrap_Estimator","Bins_array_create",\
                 "Mean_Std_calculations_One_array",\
                 "Mean_Std_calculations_Two_array",\
                 "Sigma_Calcs"]

import math
import numpy as num

def myceil(x, base=10):
    """
    Returns the upper-bound integer of 'x' in base 'base'.

    Parameters
    ----------
    x: float
        number to be approximated to closest number to 'base'

    base: float
        base used to calculate the closest 'largest' number

    Returns
    -------
    n_high: float
        Closest float number to 'x', i.e. upper-bound float.

    Example
    -------
    >>>> myceil(12,10)
      20
    >>>>
    >>>> myceil(12.05, 0.1)
     12.10000 
    """
    n_high = float(base*math.ceil(float(x)/base))

    return n_high

def myfloor(x, base=10):
    """
    Returns the lower-bound integer of 'x' in base 'base'

    Parameters
    ----------
    x: float
        number to be approximated to closest number of 'base'

    base: float
        base used to calculate the closest 'smallest' number

    Returns
    -------
    n_low: float
        Closest float number to 'x', i.e. lower-bound float.

    Example
    -------
    >>>> myfloor(12, 5)
    >>>> 10
    """
    n_low = float(base*math.floor(float(x)/base))

    return n_low

def Bootstrap_Estimator(data, statfunction=num.mean, method='module', \
    n_samples=10000, alpha=0.05, output='errorbar'):
    """
    Calcualtes confidence interval within 5 percent for 'data' array.

    Parameters
    ----------
    data: array_like, Shape (N, ...) or 1-d array_like object.
        Input data. Data points are assumed to be delineated by axis 0

    statfunction: function (data, weights=(weights, optional)) -> value
        This function should accept samples of data from 'data'. It is applied
        to these samples individually.

    method: str, optional
        Determines what method to use to estimate the CI of 'data'
        - 'method': Use module from scikits.bootstrap.
        - 'own'   : Use my own module.

    n_samples: float, optional
        The number of bootstrap samples to use (default=10000)

    alpha: float, optional
        The percentiles to use for the confidence interval (default=0.05).
        If this is a float, the returned values are (alpha/2, 1-alpha/2) 
        percentile confidence intervals. If it is an iterable, alpha is assumed 
        to be an iterable of each desired percentile.

    output: str, optional
        The format of the output. 'lowhigh' gives low and high confidence 
        interval values. 'errorbar' gives transposed abs(value-confidence 
        interval value) values that are suitable for use with matplotlib's 
        errorbar function. (default='errorbar' in this case; 'lowhigh' otherwise)

    Returns
    -------
    CI: tuple of floats
        The confidence percentiles specified by alpha
    """
    assert(method=='module' or method=='own')
    assert(data.ndim==1) # 1-dimensional array
    # Numpy array
    data = num.array(data)
    # Number elements
    n_elem = len(data)
    # Method
    if method=='own':
        data_idx  = num.random.randint(0, n_elem,(n_samples, n_elem))
        samples   = data[data_idx]
        stat_data = num.sort(statfunction(samples,1))
        CI = num.array([stat_data[int((alpha/2.)*n_samples)], \
            stat_data[int((1.-(alpha/2.))*n_samples)]]).reshape((2,1))
        if output=='errorbar':
            CI = abs(CI-statfunction(stat_data))[num.newaxis].T
    elif method=='module':
        try:
            import scikits.bootstrap as bootstrap
        except ImportError as e:
            raise Exception ('Module "bootstrap" not found')
        CI = bootstrap.ci(data=data, statfunction=statfunction, alpha=alpha,\
            output=output)

    return CI

def Bins_array_create(arr, base=10):
    """
    Generates array between [arr.min(), arr.max()] in steps of `base`.

    Parameters
    ----------
    arr: array_like, Shape (N,...), One-dimensional
        Array of numerical elements

    base: float, optional (default=10)
        Interval between bins

    Returns
    -------
    bins_arr: array_like
        Array of bin edges for given arr

    """
    base = float(base)
    arr  = num.array(arr)
    assert(arr.ndim==1)
    arr_min  = myfloor(arr.min(), base=base)
    arr_max  = myceil( arr.max(), base=base)
    bins_arr = num.arange(arr_min, arr_max+0.5*base, base)

    return bins_arr

def Mean_Std_calculations_One_array( X1_arr, Y1_arr, base=1., n_samples=10000,\
    alpha=0.05, arr_len=0, arr_digit='n', statfunction=num.mean, weights=None,\
    bin_statval='average', failval=-1.e7, return_perc=False):
    """
    Calculates statistics of two arrays, e.g. scatter, error in 'statfunction', 
    etc.

    Parameters
    ----------
    X1_arr: array_like, Shape (N, ...), One-dimensional array
        Array of x-values

    Y1_arr: array_like, Shape (N, ...), One-dimensional array
        Array of y-values

    base: float
        Value of bin width in units of that of X1_arr

    n_samples: float or int, optional (default=10000)
        Number of samples for bootstrap

    alpha: float, optional
        Confidence interval for ``statfunction``. 1.-alpha = confidence

    arr_len: int, optional (default=0)
        Minimum number of elements in bins

    arr_digit: string, optional (default='n')
        Option for what elements to return
        - `n`: Mean values of X1_arr and Y1_arr, standard dev, and mean of 
                standard dev.
        - `y`: Mean values of X1_arr and Y1_arr, standard dev, and mean of 
                standard dev,
                array of elements in bins for X1 and Y1
        - `o`: Array of elements in bins for X1 and Y1

    statfunction: statistical function, optional (default=numpy.mean)
        Numerical function to calculate on bins of data.
        - numpy.mean  : mean value for each bin + error in the mean.
        - numpy.median: median value for each bin + error in the median.

    weights: array_like, optional (default=None)
        Array of weights for values in Y1_arr.

    bin_statval: string, optional (default='average')
        Option for where to plot the bin values of X1_arr and Y1_arr.
        - 'average': Returns the x-points at the average x-value of the bin
        - 'left'   : Returns the x-points at the left-edge of the x-axis bin
        - 'right'  : Returns the x-points at the right-edge of the x-axis bin

    return_perc: boolean, optional (default = False)
        option for returning percentiles of the data
        Last item in the return List

    Returns
    -------
    X1_stat_arr: array_like
        statfunction of each bin in `base` spacings for X1_arr

    Y1_stat_arr: array_like
        statfunction of each bin in `base` spacings for Y1_arr

    Y1_std_arr: array_like
        standard deviation of values in bins for Y1_arr

    Y1_std_err_arr: array_like
        error in the statfunct (mean/median) for Y1_arr

    X1_bins_data: array_like, optional
        Elements of X1_arr in each bin with spacing of `base`

    Y1_bins_data: array_like, optional
        Elements of Y1_arr in each bin with spacing of `base`

    Note:
    -----
    if return_perc: last item in the `return` is `perc_arr_lims`
    """
    # Assertions and checks before proceeding
    assert(arr_digit=='y' or arr_digit=='n' or arr_digit=='o')
    X1_arr = num.array(X1_arr)
    Y1_arr = num.array(Y1_arr)
    assert(X1_arr.ndim==1 and Y1_arr.ndim==1)
    try: 
        assert(len(X1_arr)>0 and len(Y1_arr)>0) 
    except:
        raise AssertionError ("Arrays X and Y must have at least one value")
    n_elem = len(X1_arr)
    if weights==None: weights=num.ones(n_elem)
    assert(arr_len>=0)
    arr_len = int(arr_len-1.) if arr_len != 0 else int(arr_len)
    # Bins
    X1_bins_arr = Bins_array_create(X1_arr, base=base)
    X1_dig_arr  = num.digitize(X1_arr, X1_bins_arr)
    # Selecting data in bins
    if bin_statval=='average':
        X1_stat_arr = num.array([ statfunction(X1_arr[X1_dig_arr==ii]) if 
            len(X1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X1_bins_arr))])
    elif bin_statval=='left':
        X1_stat_arr = num.array([ X1_bins_arr[:-1][ii-1] if 
            len(X1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X1_bins_arr))])
    elif bin_statval=='right':
        X1_stat_arr = num.array([ X1_bins_arr[1:][ii-1] if 
            len(X1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X1_bins_arr))])
    Y1_stat_arr = num.array([ statfunction(Y1_arr[X1_dig_arr==ii]) if 
        len(Y1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
        in range(1, len(X1_bins_arr))])
    Y1_std_arr = num.array([ num.std(Y1_arr[X1_dig_arr==ii]) if 
        len(Y1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
        in range(1, len(X1_bins_arr))])
    Y1_std_err_arr = num.array([ 
        num.std(Y1_arr[X1_dig_arr==ii])/math.sqrt(len(Y1_arr[X1_dig_arr==ii])) if 
        len(Y1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
        in range(1, len(X1_bins_arr))])
    if arr_digit=='y' or arr_digit=='o':
        X1_bins_data = num.array([ X1_arr[X1_dig_arr==ii] if 
            len(X1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X1_bins_arr))])
        Y1_bins_data = num.array([ Y1_arr[X1_dig_arr==ii] if 
            len(Y1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X1_bins_arr))])
    # Removing failval's
    X1_failval_idx = num.where(X1_stat_arr != failval)[0]
    X1_stat_arr    = X1_stat_arr   [X1_failval_idx]
    Y1_stat_arr    = Y1_stat_arr   [X1_failval_idx]
    Y1_std_arr     = Y1_std_arr    [X1_failval_idx]
    Y1_std_err_arr = Y1_std_err_arr[X1_failval_idx]
    if arr_digit=='y' or arr_digit=='o':
        X1_bins_data   = X1_bins_data  [X1_failval_idx]
        Y1_bins_data   = Y1_bins_data  [X1_failval_idx]

    # Correcting error if statfunction == numpy.median
    if statfunction==num.median:
        Y1_std_err_arr *= 1.253

    # Returning Percentiles
    if return_perc:
        Y1_bins_data_1 = [ Y1_arr[X1_dig_arr==ii] if \
            len(Y1_arr[X1_dig_arr==ii]) > arr_len else failval for ii \
            in range(1, len(X1_bins_arr))]
        Y1_bins_data_arr = [[] for x in range(len(X1_failval_idx))]
        for ii in range(len(X1_failval_idx)):
            Y1_bins_data_arr[ii] = Y1_bins_data_1[X1_failval_idx[ii]]
        Y1_bins_data_arr = num.array(Y1_bins_data_arr)
        perc_arr_lims = Sigma_Calcs(Y1_bins_data_arr)
    # Returns
    if return_perc:
        if arr_digit=='n':
            return X1_stat_arr, Y1_stat_arr, Y1_std_arr, Y1_std_err_arr, perc_arr_lims
        elif arr_digit=='y':
            return X1_stat_arr, Y1_stat_arr, Y1_std_arr, Y1_std_err_arr, \
            X1_bins_data, Y1_bins_data, perc_arr_lims
        elif arr_digit=='o':
            return X1_bins_data, Y1_bins_data, perc_arr_lims
    else:
        if arr_digit=='n':
            return X1_stat_arr, Y1_stat_arr, Y1_std_arr, Y1_std_err_arr
        elif arr_digit=='y':
            return X1_stat_arr, Y1_stat_arr, Y1_std_arr, Y1_std_err_arr, \
            X1_bins_data, Y1_bins_data
        elif arr_digit=='o':
            return X1_bins_data, Y1_bins_data

def Mean_Std_calculations_Two_array( X1_arr, Y1_arr, X2_arr, Y2_arr, 
    base=1., n_samples=10000,\
    alpha=0.05, arr_len=0, arr_digit='n', statfunction=num.mean, weights=None,\
    bin_statval='average', failval=-1.e7):
    """
    Calculates statistics of two arrays, e.g. scatter, error in 'statfunction', 
    etc.

    Parameters
    ----------
    X1_arr: array_like, Shape (N, ...), One-dimensional array
        Array of x-values for first population

    Y1_arr: array_like, Shape (N, ...), One-dimensional array
        Array of y-values for first population

    X2_arr: array_like, Shape (N, ...), One-dimensional array
        Array of x-values for second population

    Y2_arr: array_like, Shape (N, ...), One-dimensional array
        Array of y-values for second population

    base: float
        Value of bin width in units of that of X1_arr

    n_samples: float or int, optional (default=10000)
        Number of samples for bootstrap

    alpha: float, optional
        Confidence interval for ``statfunction``. 1.-alpha = confidence

    arr_len: int, optional (default=0)
        Minimum number of elements in bins

    arr_digit: string, optional (default='n')
        Option for what elements to return
        - `n`: Mean values of X1_arr and Y1_arr, standard dev, and mean of 
                standard dev.
        - `y`: Mean values of X1_arr and Y1_arr, standard dev, and mean of 
                standard dev,
                array of elements in bins for X1 and Y1
        - `o`: Array of elements in bins for X1 and Y1

    statfunction: statistical function, optional (default=numpy.mean)
        Numerical function to calculate on bins of data.
        - numpy.mean  : mean value for each bin + error in the mean.
        - numpy.median: median value for each bin + error in the median.

    weights: array_like, optional (default=None)
        Array of weights for values in Y1_arr.

    bin_statval: string, optional (default='average')
        Option for where to plot the bin values of X1_arr and Y1_arr.
        - 'average': Returns the x-points at the average x-value of the bin
        - 'left'   : Returns the x-points at the left-edge of the x-axis bin
        - 'right'  : Returns the x-points at the right-edge of the x-axis bin

    Returns
    -------
    X1_stat_arr: array_like
        statfunction of each bin in `base` spacings for X1_arr

    Y1_stat_arr: array_like
        statfunction of each bin in `base` spacings for Y1_arr

    Y1_std_arr: array_like
        standard deviation of values in bins for Y1_arr

    Y1_std_err_arr: array_like
        error in the statfunct (mean/median) for Y1_arr

    X2_stat_arr: array_like
        statfunction of each bin in `base` spacings for X2_arr

    Y2_stat_arr: array_like
        statfunction of each bin in `base` spacings for Y2_arr

    Y2_std_arr: array_like
        standard deviation of values in bins for Y2_arr

    Y2_std_err_arr: array_like
        error in the statfunct (mean/median) for Y2_arr

    X1_bins_data: array_like, optional
        Elements of X1_arr in each bin with spacing of `base`

    Y1_bins_data: array_like, optional
        Elements of Y1_arr in each bin with spacing of `base`

    X2_bins_data: array_like, optional
        Elements of X2_arr in each bin with spacing of `base`

    Y2_bins_data: array_like, optional
        Elements of Y2_arr in each bin with spacing of `base`
    """
    # Assertions and checks before proceeding
    assert(arr_digit=='y' or arr_digit=='n' or arr_digit=='o')
    X1_arr = num.array(X1_arr)
    Y1_arr = num.array(Y1_arr)
    X2_arr = num.array(X2_arr)
    Y2_arr = num.array(Y2_arr)
    assert(X1_arr.ndim==1 and Y1_arr.ndim==1)
    assert(X2_arr.ndim==1 and Y2_arr.ndim==1)
    n_elem = len(X1_arr)
    if weights==None: weights=num.ones(n_elem)
    assert(arr_len>=0)
    arr_len = int(arr_len-1.) if arr_len != 0 else int(arr_len)
    # Minimum and maximum
    X_min = min(X1_arr.min(), X2_arr.min())
    X_max = min(X1_arr.max(), X2_arr.max())
    X_arr = num.array([X_min, X_max])
    # Bin array - First Population
    X_bins_arr = Bins_array_create(X_arr, base=base)
    # Data in bins - First Population
    X1_dig_arr  = num.digitize(X1_arr, X_bins_arr)
    # Selecting data in bins
    if bin_statval=='average':
        X1_stat_arr = num.array([ statfunction(X1_arr[X1_dig_arr==ii]) if 
            len(X1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X_bins_arr))])
    elif bin_statval=='left':
        X1_stat_arr = num.array([ X_bins_arr[:-1][ii-1] if 
            len(X1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X_bins_arr))])
    elif bin_statval=='right':
        X1_stat_arr = num.array([ X_bins_arr[1:][ii-1] if 
            len(X1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X_bins_arr))])
    Y1_stat_arr = num.array([ statfunction(Y1_arr[X1_dig_arr==ii]) if 
        len(Y1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
        in range(1, len(X_bins_arr))])
    Y1_std_arr = num.array([ num.std(Y1_arr[X1_dig_arr==ii]) if 
        len(Y1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
        in range(1, len(X_bins_arr))])
    Y1_std_err_arr = num.array([ 
        num.std(Y1_arr[X1_dig_arr==ii])/math.sqrt(len(Y1_arr[X1_dig_arr==ii])) if 
        len(Y1_arr[X1_dig_arr==ii]) > arr_len else failval for ii 
        in range(1, len(X_bins_arr))])
    if arr_digit=='y' or arr_digit=='o':
        X1_bins_data = num.array([ X1_arr[X1_dig_arr==ii] if 
            len(X1_arr[X1_dig_arr==ii]) > arr_len else [failval] for ii 
            in range(1, len(X_bins_arr))])
        Y1_bins_data = num.array([ Y1_arr[X1_dig_arr==ii] if 
            len(Y1_arr[X1_dig_arr==ii]) > arr_len else [failval] for ii 
            in range(1, len(X_bins_arr))])
    # Removing failval's
    X1_failval_idx = num.where(X1_stat_arr != failval)[0]
    X1_stat_arr    = X1_stat_arr   [X1_failval_idx]
    Y1_stat_arr    = Y1_stat_arr   [X1_failval_idx]
    Y1_std_arr     = Y1_std_arr    [X1_failval_idx]
    Y1_std_err_arr = Y1_std_err_arr[X1_failval_idx]
    if arr_digit=='y' or arr_digit=='o':
        X1_bins_data   = X1_bins_data  [X1_failval_idx]
        Y1_bins_data   = Y1_bins_data  [X1_failval_idx]

    # Correcting error if statfunction == numpy.median
    if statfunction==num.median:
        Y1_std_err_arr *= 1.253

    # Data in bins - Second Population
    X2_dig_arr  = num.digitize(X2_arr, X_bins_arr)
    # Selecting data in bins
    if bin_statval=='average':
        X2_stat_arr = num.array([ statfunction(X2_arr[X2_dig_arr==ii]) if 
            len(X2_arr[X2_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X_bins_arr))])
    elif bin_statval=='left':
        X2_stat_arr = num.array([ X_bins_arr[:-1][ii-1] if 
            len(X2_arr[X2_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X_bins_arr))])
    elif bin_statval=='right':
        X2_stat_arr = num.array([ X_bins_arr[1:][ii-1] if 
            len(X2_arr[X2_dig_arr==ii]) > arr_len else failval for ii 
            in range(1, len(X_bins_arr))])
    Y2_stat_arr = num.array([ statfunction(Y2_arr[X2_dig_arr==ii]) if 
        len(Y2_arr[X2_dig_arr==ii]) > arr_len else failval for ii 
        in range(1, len(X_bins_arr))])
    Y2_std_arr = num.array([ num.std(Y2_arr[X2_dig_arr==ii]) if 
        len(Y2_arr[X2_dig_arr==ii]) > arr_len else failval for ii 
        in range(1, len(X_bins_arr))])
    Y2_std_err_arr = num.array([ 
        num.std(Y2_arr[X2_dig_arr==ii])/math.sqrt(len(Y2_arr[X2_dig_arr==ii])) if 
        len(Y2_arr[X2_dig_arr==ii]) > arr_len else failval for ii 
        in range(1, len(X_bins_arr))])
    if arr_digit=='y' or arr_digit=='o':
        X2_bins_data = num.array([ X2_arr[X2_dig_arr==ii] if 
            len(X2_arr[X2_dig_arr==ii]) > arr_len else [failval] for ii 
            in range(1, len(X_bins_arr))])
        Y2_bins_data = num.array([ Y2_arr[X2_dig_arr==ii] if 
            len(Y2_arr[X2_dig_arr==ii]) > arr_len else [failval] for ii 
            in range(1, len(X_bins_arr))])
    # Removing failval's
    X2_failval_idx = num.where(X2_stat_arr != failval)[0]
    X2_stat_arr    = X2_stat_arr   [X2_failval_idx]
    Y2_stat_arr    = Y2_stat_arr   [X2_failval_idx]
    Y2_std_arr     = Y2_std_arr    [X2_failval_idx]
    Y2_std_err_arr = Y2_std_err_arr[X2_failval_idx]
    if arr_digit=='y' or arr_digit=='o':
        X2_bins_data   = X2_bins_data  [X2_failval_idx]
        Y2_bins_data   = Y2_bins_data  [X2_failval_idx]

    # Correcting error if statfunction == numpy.median
    if statfunction==num.median:
        Y2_std_err_arr *= 1.253

    # Returns
    if arr_digit=='n':
        return X1_stat_arr, Y1_stat_arr, Y1_std_arr, Y1_std_err_arr, \
        X2_stat_arr, Y2_stat_arr, Y2_std_arr, Y2_std_err_arr
    elif arr_digit=='y':
        return X1_stat_arr, Y1_stat_arr, Y1_std_arr, Y1_std_err_arr, \
        X2_stat_arr, Y2_stat_arr, Y2_std_arr, Y2_std_err_arr,\
        X1_bins_data, Y1_bins_data,\
        X2_bins_data, Y2_bins_data
    elif arr_digit=='o':
        return X1_bins_data, Y1_bins_data,\
        X2_bins_data, Y2_bins_data

def Sigma_Calcs(data_arr, type_sigma='perc', 
    perc_arr=num.array([68., 95., 99.7])):
    """
    Calculates the 68-, 95, and 100-percentiles for an array

    Parameters
    ----------
    data_arr: array_like
        array of values, from which to calculate percentiles

    type_sigma: string, optional (default = 'perc')
        option of calculating either percentiles or standard deviations
        options: 'std', 'perc'

    perc_arr: array-like, optional
        array of percentages to calculate

    Returns
    -------
    min_max_arr: array_like, shape ( len(perc_arr), 2)
        array of the minimum and maximum limits for all the percentages
    """
    data_arr      = num.array( data_arr )
    type_sigma    = type_sigma.lower()
    perc_arr_len  = len( perc_arr )
    perc_arr_lims = [ [[],[]] for xx in xrange(perc_arr_len)]
    ## Testing Shape of data_arr
    try:
        if type_sigma == 'perc':
            ## Calculating Percentiles
            for ii in range(perc_arr_len):
                min_val = num.nanpercentile(data_arr, 50.-(perc_arr[ii]/2.),axis=1)
                max_val = num.nanpercentile(data_arr, 50.+(perc_arr[ii]/2.),axis=1)
                perc_arr_lims[ii][0] = min_val
                perc_arr_lims[ii][1] = max_val
        elif type_sigma == 'std':
            ## Calculating Standard Deviations
            std_ii = 1.
            mean_val = num.nanmean( data_arr, axis=1 )
            std_val  = num.nanstd(  data_arr, axis=1 )
            for ii in range(perc_arr_len):
                min_val  = mean_val - (std_ii * std_val)
                max_val  = mean_val + (std_ii * std_val)
                perc_arr_lims[ii][0] = min_val
                perc_arr_lims[ii][1] = max_val
                std_ii  += 1.
        perc_arr_lims = num.array(perc_arr_lims)
    except:
        if type_sigma == 'perc':
            data_len = len(data_arr)
            perc_arr_lims = num.zeros((perc_arr_len,2,len(data_arr)))
            ## Looping over Bins
            for ii in range(data_len):
                # Looping over Percentiles
                for jj in range(perc_arr_len):
                    min_val = num.nanpercentile(data_arr[ii], 50.-(perc_arr[jj]/2.))
                    max_val = num.nanpercentile(data_arr[ii], 50.+(perc_arr[jj]/2.))
                    ## Saving Values
                    perc_arr_lims[jj][0][ii] = min_val
                    perc_arr_lims[jj][1][ii] = max_val
        elif type_sigma=='std':
            data_len = len(data_arr)
            perc_arr_lims = num.zeros((perc_arr_len,2,len(data_arr)))
            ## Looping over Bins
            for ii in range(data_len):
                mean_ii = num.nanmean(data_arr[ii])
                std_ii  = num.nanstd( data_arr[ii])
                # Looping over Percentiles
                for jj in range(perc_arr_len):
                    min_val = mean_ii - std_ii
                    max_val = mean_ii + std_ii
                    ## Saving Values
                    perc_arr_lims[jj][0][ii] = min_val
                    perc_arr_lims[jj][1][ii] = max_val

    perc_arr_lims = num.array(perc_arr_lims)

    return perc_arr_lims
