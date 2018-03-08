# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 18:18:26 2018

@author:    Andreas Spielhofer
            Ph.D. Candidate
            Physics Departement
            McGill University
            Montreal, Canada
@contact:   andreas.spielhofer@mail.mcgill.ca
"""

import numpy as np
from scipy.optimize import curve_fit
import pylab as plt
import math


N = 1000 # number of data points
t = np.linspace(0, 2*np.pi, N) #this would be your x-data (steps) from your arduino
data = 255*np.sin(2*np.pi*t+1/4*np.pi) # this would be your y-data from your arduino (Amplitude)


# play around with this guess values until you get a good fit
guess_freq = 5 #change it from 5 to 3 or 2.7 to see what happens
guess_amplitude = np.std(data)/(2**0.5)
guess_phase = 0
guess_offset = np.mean(data)


p0=[guess_freq, guess_amplitude,
    guess_phase, guess_offset]

# create the function we want to fit
def my_cos2(x, freq, amplitude, phase, offset):
    return np.cos(x * freq + phase)**2 * amplitude + offset

# now do the fit
fit = curve_fit(my_cos2, t, data, p0=p0)

# we'll use this to plot our first estimate. This might already be good enough for you
data_first_guess = my_cos2(t, *p0)

# recreate the fitted curve using the optimized parameters
data_fit = my_cos2(t, *fit[0])
print fit[0]

plt.plot(data, '.')
plt.plot(data_fit, label='after fitting')
plt.plot(data_first_guess, label='first guess')
plt.legend()
plt.show()
