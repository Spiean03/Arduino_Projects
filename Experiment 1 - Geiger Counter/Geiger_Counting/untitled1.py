#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:58:27 2018

@author: aaron.mascaro
"""

import matplotlib.pyplot as p
import numpy as np

    # change nn to your group number
#path = '/mnt/home/phys339-nn/Geiger_Counting'
path = '/mnt/home/amasca/geiger_2018/Geiger_Counting/'

    # change to proper filename
#filename = '2018_01_23_HH_MM_SS_COUNTING_DATA'
filename = '2018_01_22_17_11_16_COUNTING_DATA'
 
data = np.loadtxt(path+filename)

numBins = np.size(data[1,:])
bins = range(numBins)

    #plot a histogram of the data:
p.bar(bins,np.mean(data,axis=0))

yerr = np.std(data,axis=0)
p.errorbar(bins,np.mean(data,axis=0),yerr,ls = 'none',color='k')
