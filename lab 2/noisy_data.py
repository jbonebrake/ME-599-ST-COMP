# -*- coding: utf-8 -*-
#!usr/bin/env python 3
"""
Created on Wed Jan 23 10:53:56 2019

@author: jbonebrake
"""

# =============================================================================
# Code for lab 2, tasks 4 and 6
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

from sensor import generate_sensor_data
from null_filter import apply_null_filter
from filters import mean_filter
from writefile import write_file

n = 256
x = np.linspace(1,n-1,n)
sigma = 0.1

data = []

# use generator function to acquire noisy data
for d in generate_sensor_data(n,sigma):
    data = data + [d]

# apply mean filter with a few different widths  
data_null = apply_null_filter(data)
data_filt_3 = mean_filter(data,3)
data_filt_7 = mean_filter(data,7)
data_filt_11 = mean_filter(data,11)

# write unfiltered and filtered data to file
filepath_noisy = 'C:\\Users\\jmich\\.spyder-py3\\ME 599\\lab 2\\noisy_data.txt'
filepath_null = 'C:\\Users\\jmich\\.spyder-py3\\ME 599\\lab 2\\null_filt_data.txt'
filepath_mean = 'C:\\Users\\jmich\\.spyder-py3\\ME 599\\lab 2\\mean_filt_data.txt'

write_file(data,filepath_noisy)
write_file(data_null,filepath_null)
write_file(data_filt_3,filepath_mean)

# generate some plots to compare unfiltered and filtered data
plt.figure()
plt.plot(x,data)
plt.scatter(x,data_null,c = 'r')
plt.legend(['unfiltered','null-filtered'])


plt.figure()
plt.plot(x,data)
plt.scatter(x[1:-1],data_filt_3,c = 'r')
plt.legend(['unfiltered','mean-filtered, w = 3'])

plt.figure()
plt.plot(x,data)
plt.scatter(x[3:-3],data_filt_7,c = 'r')
plt.legend(['unfiltered','mean-filtered, w = 5'])

plt.figure()
plt.plot(x,data)
plt.scatter(x[5:-5],data_filt_11,c = 'r')
plt.legend(['unfiltered','mean-filtered, w = 11'])
