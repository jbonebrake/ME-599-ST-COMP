# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 4, exercise 1
# Jonathan Bonebrake

def sin(x):
    import matplotlib.pyplot as mpl
    import numpy as np
    y = np.sin(x)
    mpl.figure()
    mpl.plot(x,y)
    mpl.xlabel('x')
    mpl.ylabel('sin(x)')



