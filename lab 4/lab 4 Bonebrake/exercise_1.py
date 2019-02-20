# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 4, Exercise 1
# Jonathan Bonebrake

def plot_1(x):
    import matplotlib.pyplot as mpl
    import numpy as np

    y = np.sin(x)
    
    mpl.figure()
    mpl.plot(x/np.pi,y)
    mpl.xlabel(r'$\pi$')
    mpl.ylabel('sin(x)')
    mpl.axis([0, 4, -1, 1])
    mpl.title('Exercise 1: Gratuitously Tight Sine Plot')