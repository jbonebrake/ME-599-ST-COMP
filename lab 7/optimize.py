# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 7
# Jonathan Bonebrake

import numpy as np
import random


def optimize_step(f,bounds,n):
    
    x = np.linspace(bounds[0],bounds[1],n)
    y = eval(f)
    ymax = np.max(y)
    
    return ymax
    
def optimize_random(f,bounds,n):
    x = []
    for n in range(n):
        x = np.append(x,random.uniform(bounds[0],bounds[1]))
    y = eval(f)
    ymax = np.max(y)
    
    return ymax

if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    import numpy as np
    import random 
    
    f = 'cos(x)*x**2'
    bounds = (0,100)
    steps = [10, 50, 100, 200, 500, 1000]
    max_step =[]
    max_random = []
    
    for n in steps:
        max_step = np.append(max_step, optimize_step(f,bounds,n))
        max_random = np.append( max_random, optimize_random(f,bounds,n))
    x = np.linspace(bounds[0],bounds[1],1000) 
    y = eval(f)
    
    plt.figure()    
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    
    plt.figure()    
    plt.plot(steps,max_step)
    plt.plot(steps,max_random)
    plt.legend(['uniform increment','random increment'])
    plt.xlabel('number of evaluations')
    plt.ylabel('estimated maximum')
    plt.show()