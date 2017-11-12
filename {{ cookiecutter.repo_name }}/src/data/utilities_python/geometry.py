#! /usr/bin/env python

# Victor Calderon
# February 14, 2016
# Vanderbilt University

"""
Set of geometrical definitions for translations, 
coordinate transformations, etc.
"""
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, geometry"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
__all__        =["flip_angles", "Ang_Distance", "Coord_Transformation"]

import numpy as num

def flip_angles(ang, unit='deg'):
    """
    Ensures that angle is between 0 to 360 degrees.

    Parameters
    ----------
    ang: float
          Angle in degrees

    unit: str, optional
            Unit of the angle 'ang'.
            'ang' can only be in 'deg' or 'rad' units.

    Returns
    -------
    ang: float
            Angle between 0 and 360 degrees.

    Raises
    ------
    ValueError
        when 'ang' is not a digit and a float/int number.
    """
    assert(unit=='deg' or unit=='rad')
    # Checking type of `ang'
    if isinstance(ang, float) or isinstance(ang, int):
        ang = float(ang)
        if ang < 0:
            ang += 360.
        if unit=='rad':
            ang = num.radians(ang)
    else:
        try:
            ang = num.array(ang)
            ang = num.array([xx if xx >= 0 else xx+360. for xx in ang])
            if unit=='rad':
                ang = num.radians(ang)
        except ValueError: raise ValueError( "'{0}' is not a float".format(ang))

    return ang

def Ang_Distance( ra1, ra2, dec1, dec2, unit='deg', method='haversine'):
    """
    Calculates angular separation between two points with given right ascensions
    and declinations.
    -Taken from: https://en.wikipedia.org/wiki/Haversine_formula

    Parameters
    ----------
    ra1: float
            Right ascension of the 1st point.
            Units in degrees by default.

    ra2: float
            Right ascension of the 2nd point.
            Units in degrees by default.

    dec1: float
            Decliantion of the 1st point.
            Unit in degrees by default.

    dec2: float
            Declinatin of 2nd point.
            Unit in degrees by default.

    unit: str, optional
            Unit of the angles.
            Units by default in 'deg'. Optons: 'deg' or 'rad'.

    method: str, optional
            Method used to calculate angular distance.
            Default: 'haversine'. Options: 'haversine', 'astropy'

    Returns
    -------
    ang_h: float
            Angular distance between 1st and 2nd point.
            In 'degrees'

    Notes
    -----
    A = 90 - dec2
    B = 90 - dec1
    D = ra1 - ra2
    c = Angle between two points
    """
    assert(method=='haversine' or method=='astropy')
    ra1  = flip_angles(ra1 , unit=unit)
    ra2  = flip_angles(ra2 , unit=unit)
    # dec1 = flip_angles(dec1, unit=unit)
    # dec2 = flip_angles(dec2, unit=unit)

    if method=='haversine':
        A = num.radians(90.-dec1)
        B = num.radians(90.-dec2)
        D = num.radians(ra1-ra2 )
        
        ang_h = (num.sin((A-B)*.5))**2. + num.sin(A)*num.sin(B)*(num.sin(D*.5))**2.
        ang_h = num.degrees(2*num.arcsin(ang_h**0.5))

    if method=='astropy':
        from astropy import coordinates as coord
        from astropy.coordinates import SkyCoord
        from astropy import units as u

        if unit=='deg': 
            unit_opt = u.degree
        elif unit=='rad':
            unit_opt == u.radians

        P1    = SkyCoord(ra=ra1, dec=dec1, unit=(unit_opt, unit_opt))
        P2    = SkyCoord(ra=ra2, dec=dec2, unit=(unit_opt, unit_opt))
        ang_h = P1.separation(P2)
        ang_h = ang_h.degree

    return ang_h

def Coord_Transformation(ra_arr, dec_arr, dist_arr, ra_cen, dec_cen, dist_cen, 
    trans_opt=4):
    """
    Transforms spherical coordinates (ra,dec,dist) into cartesian coordinates.
    It centers the array about the center of the distribution

    Parameters
    ----------
    ra_arr: array_like
            Array of right ascensions of elements.
            Units in degrees by default.

    dec_arr: array_like
            Array of declinations of elements.
            Units in degrees by default.

    dist_arr: array_like
            Array of distance of elements from observer.
            No unit dependent.

    ra_cen: float
            Right ascension value of the center of distributions.
            Unit in degrees by default.

    dec_cen: float
            Declination value of the center of distribution.
            Unit in degrees by default.

    dist_cen: float
            Distance value from observer to center of distribution.
            No unit dependent.

    trans_opt: int
            Option for cartesian translation/transformation for elements.
            By default, trans_opt=4
            Options:
                1 - No translation involved
                2 - Translation to the center point
                3 - Translation and rotation to the center point
                4 - Translation and two rotations about the center point

    Returns
    -------
    sph_dict: python dict
            Python dictionary with spherical coords of elements based on 
            'trans_opt' value.
            Keys=['RA', 'DEC', 'CZ']

    coord_dict: python dict
            Python dictionary with cartesian coords of elements based on 
            'trans_opt' value.
            Keys=['X', 'Y', 'Z']
    """
    ra_cen   = flip_angles(float(ra_cen))
    dec_cen  = flip_angles(float(dec_cen))
    dist_cen = float(dist_cen)

    # Check number of elements
    if isinstance(ra_arr, float) or isinstance(ra_arr, int):
        assert( isinstance(ra_arr,float) or isinstance(ra_arr,int))
        ra_arr   = num.array([ra_arr])
        dec_arr  = num.array([dec_arr])
        dist_arr = num.array([dist_arr])
    else:
        ra_arr   = num.array(ra_arr)
        dec_arr  = num.array(dec_arr)
        dist_arr = num.array(dist_arr)
    # Dict of angular position
    dict_keys_cart = ['RA','DEC','CZ']
    sph_dict = dict(zip(dict_keys_cart,num.vstack((ra_arr,dec_arr,dist_arr))))
    ## Number of elements
    n_elem   = len(ra_arr)
    ## Spherical-to-Cartesian transformation - center
    X0_cen = float(dist_cen*num.cos(num.radians(ra_cen))*num.cos(num.radians(dec_cen)))
    Y0_cen = float(dist_cen*num.sin(num.radians(ra_cen))*num.cos(num.radians(dec_cen)))
    Z0_cen = float(dist_cen*num.sin(num.radians(dec_cen)))
    ## Spherical-to-Cartesian transformation - elements
    X0_arr = dist_arr*num.cos(num.radians(ra_arr))*num.cos(num.radians(dec_arr))
    Y0_arr = dist_arr*num.sin(num.radians(ra_arr))*num.cos(num.radians(dec_arr))
    Z0_arr = dist_arr*num.sin(num.radians(dec_arr))
    ## Rotations
    # Centering
    X1_arr = X0_arr - X0_cen
    Y1_arr = Y0_arr - Y0_cen
    Z1_arr = Z0_arr - Z0_cen
    # Rotations about z- and x-axis by tau and omega
    # Rotating the poins, not the axes.
    omega = num.radians(90.-ra_cen)
    tau   = num.radians(90.-dec_cen)
    # Rotation about z-axis by omega
    X2_arr = X1_arr*num.cos(omega)-Y1_arr*num.sin(omega)
    Y2_arr = X1_arr*num.sin(omega)+Y1_arr*num.cos(omega)
    Z2_arr = Z1_arr.copy()
    # Rotation about x-axis by tau
    X3_arr = X2_arr.copy()
    Y3_arr = Y2_arr*num.cos(tau)-Z2_arr*num.sin(tau)
    Z3_arr = Z2_arr*num.sin(tau)+Z2_arr*num.cos(tau)
    ## Saving to dictionary
    dict_keys_cart = ['X','Y','Z']
    if trans_opt==1:
        # Without translation
        coord_dict = dict(zip(dict_keys_cart,num.vstack((X0_arr, Y0_arr, Z0_arr))))
    elif trans_opt==2:
        # With translation
        coord_dict = dict(zip(dict_keys_cart,num.vstack((X1_arr, Y1_arr, Z1_arr))))
    elif trans_opt==3:
        # With translation and rotation
        coord_dict = dict(zip(dict_keys_cart,num.vstack((X2_arr, Y2_arr, Z2_arr))))
    elif trans_opt==4:
        # with translation and two rotations
        # Centered about the center of the distribution
        coord_dict = dict(zip(dict_keys_cart,num.vstack((X3_arr, Y3_arr, Z3_arr))))
    
    return sph_dict, coord_dict
