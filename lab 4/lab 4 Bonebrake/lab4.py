# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 4
# Jonathan Bonebrake

import numpy as np
import matplotlib.pyplot as mpl

# exercise 1
x = np.pi*np.linspace(0,4,200)
from exercise_1 import plot_1
plot_1(x)

#exercise 2
from rand_dist_sample import sum_10
sums = sum_10(10000)
mpl.figure()
mpl.hist(sums,100)
mpl.xlabel('value')
mpl.ylabel('occurrence')
mpl.title('Exercise 2: Histogram of Randomly Sampled Uniform Dist.')

#exercise 3
from msd import MassSpringDamper

system = MassSpringDamper(m=1.0, k=2.0, c=2.0)
state,t = system.simulate(0.0, -1.0)

mpl.figure()
mpl.plot(t,state[:,1])
mpl.xlabel('time (s)')
mpl.ylabel('position (m)')
mpl.title('Exercise 3: Simulated SMD System')

#exercise 4
import timeit
from math import pow
from exercise_4 import random_list
from exercise_4 import how_long

#increment = [1,10,100,1000,10000,100000,1000000]
# Note: I'm using a shortened range of list lengths here, because the 
# operations take a really long time. The 1,000,000 element list
# requires ~1.5 days to sort on my computer. 

increment = [1,10,100]
time_sort = []
time_sum = []

# Timing loop
for n in range(len(increment)):
    number_list = random_list(increment[n])
    time_sort = np.append(time_sort,timeit.timeit('number_list.sort()',globals = globals()))
    time_sum = np.append(time_sum, timeit.timeit('sum(number_list)',globals = globals()))
    print('sort: ' + str(time_sort))
    print('sum: ' + str(time_sum))
    

mpl.figure()
mpl.plot(increment,time_sort,'-b')
mpl.plot(increment,time_sum,'-r')
mpl.legend(('sorting','summation'),loc = 'upper left')
mpl.xlabel('number of elements')
mpl.ylabel('time (s)')

mpl.title('Sum time increases with len(list), and takes ~7x longer than sort()')
