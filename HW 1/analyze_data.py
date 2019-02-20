# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 3
# Jonathan Bonebrake


import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#print(sys.argv[1])
#test_df = pd.read_csv(sys.argv[1])
#print(filename)
#test_df = pd.read_csv(filename)
#
#time = list(test_df.Time)
#position = list(test_df.Position)
    
def analyze_data(position, time):
    c_initial = position[0]
    c_final = position[-1]
    c_max = max(position)
    c_min = min(position)
    overshoot = 100*c_max/abs(c_initial-c_final)
    #index_max = max(range(len(position)), key=position.__getitem__)
    index_max = np.argmax(position)
    
    # shift data so that all values are positive
    pseudo_pos = [p+2*(c_final-c_min) for p in position]
    #print(str(c_max-c_min))
    p_initial = pseudo_pos[0]
    p_final = pseudo_pos[-1]


    #find index of first value greater than 0.1(p_initial) and 0.9(p_initial)
    #if not found, returns 1000
    t_10 = time[next((i for i in range(len(time)) if pseudo_pos[i] > 0.1*abs(p_final-p_initial)),1000)]
    t_90 = time[next((i for i in range(len(time)) if pseudo_pos[i] > 0.9*abs(p_final-p_initial)),1000)]    
    
    plt.figure()
    plt.plot(time,position)
    
    return c_initial, c_final, overshoot, t_10, t_90, pseudo_pos, p_final        
            

    
    print('c_initial: ' + str(c_initial))
    print('c_final: ' + str(c_final))
    print('c_max: ' + str(c_max))
    print('overshoot: ' + str(overshoot)+ '%')
    print('peak time: ' + str(time[index_max]))
    print('t_10: ' + str(t_10))
    print('t_90: ' + str(t_90))
    print('rise time: ' + str(t_90-t_10))
    #print('p_initial: ' + str(p_initial))
    #print('p_final: ' + str(p_final))
    
    #return time, position
def time_chop(time,data,percent):
    #import time
    #initial = len(data)
    upper = (percent/100)*(max(data)-data[-1])
    lower = -upper
    #time.sleep(5)
    print('max bound: '+ str(upper))
    print('min bound: '+ str(lower))
    #count = 0
    
    while max(data) >= upper and min(data) <= lower:
        time = time[1:]
        data = data[1:]
    print(len(data))
    print(min(data))
    print(max(data))
    plt.plot(time,data)

    return time, data, time[0]
    
#    if max(data) <= upper and min(data) >= lower:
#        print('success')
#        print(max(data))
#        print(min(data))
#        return data
#    else:
#        #count = count + 10
#        #print(str(count))
#        print('max: ' + str(max(data)))
#        print('min: ' + str(min(data)))
#        print(len(data))
#        
#        time_chop(data[1:],upper,lower)
 


        
filename = 'data1.csv'
print(filename)
test_df = pd.read_csv(filename)

time = list(test_df.Time)
position = list(test_df.Position)
    
c_initial, c_final, overshoot, t_10, t_90, pseudo_pos,p_final = analyze_data(position,time)
crop_time, crop_data,t_s = time_chop(time,position,2)

zeta = -np.log(overshoot/100)/np.sqrt(np.pi**2 + (np.log(overshoot/100))**2)
omega_n = 4*zeta/t_s
c = 2*zeta*omega_n
k = omega_n**2

#check some things
from msd import MassSpringDamper
system = MassSpringDamper(m=1.0, k=k, c=c)
state,t = system.simulate(c_initial,0)