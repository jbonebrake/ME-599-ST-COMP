# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 3
# Jonathan Bonebrake

import sys




def data_parse(filename):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    test_df = pd.read_csv(filename)
    time = list(test_df.Time)
    position = list(test_df.Position)
    c_initial = position[0]
    c_final = position[-1]
    c_max = max(position)
    
    plt.figure()
    plt.plot(time,position)
    
    print('c_initial:' + str(c_initial))
    print('c_final:' + str(c_final))
    print('c_max:' + str(c_max))
    
    return time, position
    


