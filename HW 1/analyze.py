# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 HW 1
# Jonathan Bonebrake

def analyze_data(filename):
    import pandas as pd
    import numpy as np
    
    # read in data from file, split into time, position
    data = pd.read_csv(filename)
    time = list(data.Time)
    position = list(data.Position)
    # determine initial, final, maximum, minumum, overshoot values
    c_initial = position[0]
    c_final = position[-1]
    c_max = max(position)
    #c_min = min(position)
    index_max = np.argmax(position) # index for maximum value
    #find index of first value greater than 0.1(p_initial) and 0.9(p_initial)
    #if not found, returns 100000
    t_10 = time[next((i for i in range(len(time)) if (position[i]) >= 0.1*(c_initial-c_final)),100000)]
    t_90 = time[next((i for i in range(len(time)) if (position[i]) >= 0.9*(c_initial-c_final)),100000)]    
    #find corresponding peak time    
    t_peak = time[index_max]
    t_rise = t_10-t_90
    #calculate percent overshoot
    overshoot = 100*c_max/abs(c_initial-c_final)
    
    # Calculate 2% rise time
    # change 'percent' value in case different rise time is needed 
    percent = 2
    # upper bound uses the maximum absolute displacement from c_final 
    # to calculate 2% displacement bound
    upper = (percent/100)*(max(np.absolute(position))-position[-1])
    lower = -upper
    while max(position) >= upper and min(position) <= lower:
        # remove elements until criteria met
        time = time[1:]
        position = position[1:]
    # find first time at which percent criteria met    
    t_settle = time[0]
    return c_initial, c_max, c_final, t_rise, t_peak, overshoot, t_settle

    
def estimate_system(filename):
    import numpy as np

    # get system characteristics 
    c_initial, c_max, c_final, T_r, T_p, percentOS, T_s = analyze_data(filename)
    # calcylate zeta, omega_n from controls book equations
    zeta = -np.log(percentOS/100)/np.sqrt(np.pi**2 + (np.log(percentOS/100))**2)
    omega_n = 4*zeta/T_s
    # estimate c, k for m = 1 system
    c = 2*zeta*omega_n
    k = omega_n**2 
    
    return 1,c,k

# code below for running from command line 
import sys
import numpy as np

try:
    #print(sys.argv[1])
    c_initial, c_max, c_final, T_r, T_p, percentOS, T_s = analyze_data(sys.argv[1])
    m,c,k = estimate_system(sys.argv[1])
    zeta = -np.log(percentOS/100)/np.sqrt(np.pi**2 + (np.log(percentOS/100))**2)
    omega_n = 4*zeta/T_s

    print('filename: ' + str(sys.argv[1]))
    print('Peak time: ' + str(round(T_p,3))+'s')
    print('Percent overshoot: ' + str(round(percentOS,2)) + '%')
    print('Settling time: ' +str(round(T_s,3)) + 's')
    print('Omega_n: ' + str(round(omega_n,3)))
    print('Zeta: ' + str(round(zeta,3)))
    print('Spring constant: ' + str(k))
    print('Mass: '+ str(m))
    print('Damper: '+ str(c))
    
except TypeError :
    print('running as script')

except IndexError:
    print('running as script')    


## code below for testing in IDE ( shorter file, and bypassing argv.sys...)
#if __name__ == '__main__':
#    
#    print('testdata')
#    c_initial, c_max, c_final, T_r, T_p, percentOS, T_s = analyze_data('testdata.csv')
#    m,c,k = estimate_system('testdata.csv')
#    zeta = -np.log(percentOS/100)/np.sqrt(np.pi**2 + (np.log(percentOS/100))**2)
#    omega_n = 4*zeta/T_s
#
#    print('Peak time: ' + str(round(T_p,3)))
#    print('Percent overshoot: ' + str(round(percentOS,2)) + '%')
#    print('Settling time: ' +str(round(T_s,3)) + 's')
#    print('Omega_n: ' + str(round(omega_n,3)))
#    print('Zeta: ' + str(round(zeta,3)))
#    print('Spring constant: ' + str(k))
#    print('Mass: '+ str(m))
#    print('Damper: '+ str(c))