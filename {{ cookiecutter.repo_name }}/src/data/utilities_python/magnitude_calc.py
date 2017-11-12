#! /usr/bin/env python

# Victor Calderon
# February 18, 2016
# Vanderbilt University

"""
Computes different quantities regarding magnitude conversions.
"""

from __future__ import division, print_function, absolute_import
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, magnitude_calc"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
__all__        =["apparent_to_absolute_magnitude",\
                 "absolute_to_apprent_magnitude",\
                 "get_sun_mag",\
                 "absolute_magnitude_to_luminosity",\
                 "luminosity_to_absolute_mag",\
                 "absolute_magnitude_lim"]

import numpy as num

def apparent_to_absolute_magnitude(mag, d):
    """
    Calculates the absolute magnitude using the luminosity and apparent mag.

    Parameters
    ----------
    mag: array_like
        Array of apparent magnitude(s)

    d: array_like
        Array of luminosity distance to object. 
        In units of Mpc.

    Returns
    -------
    Mag: array_like
        Numpy array of absolute magnitudes
    """
    mag = num.array(mag)
    d   = num.array(L  )
    Mag = mag - 5.*(6.+num.log10(d))+5.

    return Mag

def absolute_to_apprent_magnitude(Mag, d):
    """
    Calculates the apparent magnitude using the luminosity and absolute mag.

    Parameters
    ----------
    Mag: array_like
        Array of apparent magnitudes

    d: array_like
        Array of luminosity distance to object. 
        In units of Mpc.

    Returns
    -------
    mag: array_like
        Numpy array of apparent magnitude(s).
    """

    Mag = num.array(Mag)
    d   = num.array(d  )
    mag = Mag +5.*(6.+num.log10(d))-5.

    return mag

def get_sun_mag(filter,system='SDSS_Blanton_2003_z0.1'):
    """
    Get solar absolute magnitudes for a filter in a system.
    Taken from Duncan Campbell, and later modified.
    
    Parameters
    ----------
    filter: string
        magnitude filter to use.
    
    system: string
        Kind of filter to use. (default = `SDSS_Blanton_2003_z0.1`)
        Options: 
        - `Binney_and_Merrifield_1998`: See Binney and Merrifield 1998
        - `SDSS_Blanton_2003_z0.1`: See Blanton et al. 2003 equation 14
    
    Returns
    -------
    Msun: float
        Solar absolute magnitude in `filter` using `system`.
    """
    if system=='Binney_and_Merrifield_1998':
        if filter=='U':
            return 5.61
        elif filter=='B':
            return 5.48
        elif filter=='V':
            return 4.83
        elif filter=='R':
            return 4.42
        elif filter=='I':
            return 4.08
        elif filter=='J':
            return 3.64
        elif filter=='H':
            return 3.32
        elif filter=='K':
            return 3.28
        else:
            raise ValueError('Filter does not exist in this system.')
    if system=='SDSS_Blanton_2003_z0.1':
        if filter=='u':
            return 6.80
        elif filter=='g':
            return 5.45
        elif filter=='r':
            return 4.76
        elif filter=='i':
            return 4.58
        elif filter=='z':
            return 4.51
        else:
            raise ValueError('Filter does not exist in this system.')
    else:
        raise ValueError('Filter system not included in this package.')

def absolute_magnitude_to_luminosity(Mag, band, system='SDSS_Blanton_2003_z0.1'):
    """
    Calculates the luminosity of the object through `band` filter

    Parameters
    ----------
    Mag: array_like
        Array of absolute magnitudes in filter `band`.
    
    band: string
       filter band
    
    system: string, optional
        filter systems: default is 'SDSS_Blanton_2003_z0.1'
          1. Binney_and_Merrifield_1998
          2. SDSS_Blanton_2003_z0.1
    
    Returns
    -------
    logL: array_like
        Array of log values of luminosities.
        In units of log(L/Lsun)
    """
    Msun = get_sun_mag(band, system)
    logL = (Msun-Mag)*0.4

    return logL

def luminosity_to_absolute_mag(L, band, system='SDSS_Blanton_2003_z0.1'):
    """
    Calculates the absolute magnitude of object through the `band` filter.

    Parameters
    ----------
    L: array_like
        Array of luminosities

    band: string
        filter band

    system: string, optional
        filter systems: default is 'SDSS_Blanton_2003_z0.1'
          1. Binney_and_Merrifield_1998
          2. SDSS_Blanton_2003_z0.1

    Returns
    -------
    Mag: array_like
        Array of absolute magnitude(s) through `band` filter
    """
    Msun = get_sun_mag(band, system)
    Lsun = 1.0 # In units of solar luminosities
    Mag  = Msun -2.5*num.log10(L/Lsun)

    return Mag

def absolute_magnitude_lim(z, mag_lim, cosmo=None):
    """
    Calculates the absolute magnitude limit as function of redshift for a 
    flux-limited survey

    Parameters
    ----------
    z: float
        redshift

    mag_lim: float
        apparent magnitude limit

    cosmo: cosmology object
        From astropy.cosmology

    Return
    ------
    Mag: array_like
        Absolute magnitude limit in units of Mag + 5*log(h).
    """
    if cosmo==None:
        from astropy.cosmology import FlatLambdaCDM
        cosmo=FlatLambdaCDM(H0=70, Om0=0.316)
        print(">> Warning: No cosmology was specified. Using default:",cosmo)
    d = cosmo.luminosity_distance(z).value
    Mag = apparent_to_absolute_magnitude(mag_lim, d)

    return Mag
