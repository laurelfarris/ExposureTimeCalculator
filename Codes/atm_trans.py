'''
Atmospheric transmission, a (extinction, refraction, etc.)
'''

import numpy as np
import math
from astropy import constants as const

''' Define constants '''
c = const.c.cgs.value
h = const.h.cgs.value

def atm_transmission(bandpass, object_mag, airmass)
    '''
    Calculate the atmospheric transmission (a),
    which should be between 0 and 1
    (fraction of total light from object that made it through the atmosphere).

      ``the amount of light lost [magnitudes] can be specified by a
        set of extinction coefficients''.

    net_mag is the magnitude at the bottom of the atmosphere,
    k is the (POSITIVE) extinction coefficient, to be read in from a file
    using the bandpass information (still need to figure out how to do this).
    '''

    '''
    Open files (path is RELATIVE at the moment... better to do this
    differently? Or put the input files in the same directory as the
    codes themselves?
    '''
    f = open('../Input_files/extinction.txt')
    for line in f:
        if not line.strip().startswith("#"):
            wavelength,k = np.loadtxt(f, unpack=True)

    '''
    Math (not to be used in actual code)
    This work is from the class notes under
    'Airmass and zenith distance dependence'.
    '''
    net_mag = object_mag + k*airmass
    net_mag - object_mag = -2.5*math.log10(net_flux/object_flux)
    net_mag - object_mag = -2.5*math.log10(a)
    a = 10.^((net_mag - object_mag)/-2.5)
    a = 10.^((k*airmass)/-2.5)

    ''' Value to be returned in code '''
    return 10.^(k*airmass / -2.5)

