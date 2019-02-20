# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 4: exercise 4
# Jonathan Bonebrake

def random_list(increment):
    import random
    import numpy as np
    numbers = []
    
    for m in range(increment):
        numbers = np.append(numbers, random.random()/random.random())
    return list(numbers)

def how_long(number_list):
    import timeit
    import numpy as np    
    time_sort = []
    time_sum = []
          
#    time_sort = np.append(time_sort,timeit.timeit('number_list.sort()',globals = None))
#    time_sum = np.append(time_sum, timeit.timeit('sum(number_list)',globals = None))
    time_sort = np.append(time_sort,timeit.timeit('number_list.sort()',globals = globals()))
    time_sum = np.append(time_sum, timeit.timeit('sum(number_list)',globals = globals()))
    return time_sort, time_sum



