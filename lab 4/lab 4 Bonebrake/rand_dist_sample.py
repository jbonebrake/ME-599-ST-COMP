# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# function for ME 599 lab 4, exercise 2
# Jonathan Bonebrake

def sum_10(n):
    import numpy as np
    sums = []
    for i in range(n):
        sum = 0
        for j in range(10):
            # pull value from uniform dist., and add to total
            sum = sum + np.random.uniform(0,1)
        sums = np.append(sums,sum)
    return sums

        

