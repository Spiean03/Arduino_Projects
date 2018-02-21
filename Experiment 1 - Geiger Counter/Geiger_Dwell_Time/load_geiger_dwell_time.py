#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:58:27 2018

@author: aaron.mascaro
"""

import matplotlib.pyplot as p
import numpy as np

    # change nn to your group number
#path = '/mnt/home/phys339-nn/Geiger_Dwell_Time/'
path = '/mnt/home/amasca/geiger_2018/Geiger_Dwell_Time/'

    # change to proper filename
#filename = '2018_01_23_HH_MM_SS_DWELL_TIME_DATA'
filename = '2018_01_22_17_58_26_DWELL_TIME_DATA'
 
data = np.loadtxt(path+filename)

numBins = 10

    #plot a histogram of the data:
n = np.zeros((np.size(data[:,0]),numBins))
bins = np.zeros((np.size(data[:,0]),numBins+1))

 #first get the number of bins so we can properly bin ALL the data
 # (i.e. make sure each replica will fit into the bins we choose)
(_,bins) = np.histogram(data.ravel())

#Now iterate over each replica and bin it using the histogram function
for i in range(np.size(data[:,0])):
    (n[i,:],_) = np.histogram(data[i,:],bins)

#Plot the average histogram of all the replicas
p.bar(bins[0:numBins],np.mean(n,axis=0),width = (bins[2]-bins[1]))

    #a quick hack to get errorbars onto your plot
yerr = np.std(n,axis=0)/np.sqrt(np.size(data[:,0]))
p.errorbar(bins[0:numBins],np.mean(n,axis=0),yerr,ls = 'none',color='k')
