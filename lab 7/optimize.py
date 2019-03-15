# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 7
# Jonathan Bonebrake

import numpy as np
import random

def optimize_step(f,bounds,n):
    values = list()
    x = np.linspace(bounds[0],bounds[1],n)
    #y = eval(f)        
    y = f(x)
    for n in range(len(x)):
        values.append((x[n],y[n]))
    
    max_value = values[0]
    for n in range(len(values)):
        if values[n][1] >= max_value[1]:
            max_value = values[n]
            
    return max_value       
    
def optimize_random(f,bounds,n):
    x = []
    values = list()
    for n in range(n):
        x = np.append(x,random.uniform(bounds[0],bounds[1]))
    #y = eval(f)
    y = f(x)
    for n in range(len(x)):
        values.append((x[n],y[n]))
            
    max_value = values[0]
    for n in range(len(values)):
        if values[n][1] >= max_value[1]:
            max_value = values[n]
                
    return max_value       
     
## Functions for multi-dimensional function optimization 

def divide_bounds(bounds,point):
    #calculate new bounds above and below given point
    upper_bounds = ()
    lower_bounds = ()   
    for n in range(len(bounds)):        
        upper_bounds = upper_bounds + ((point[n],bounds[n][1]),)
        lower_bounds = lower_bounds + ((bounds[n][0],point[n]),)        
    return lower_bounds,upper_bounds    

def eval_func_rand(f,bounds,n_eval):
    # evaluate function randomly within given bounds, return maximum value
    import random
    values = list()
    for i in range(n_eval):
        # initialyze tuple of dependent variables
        inputs = ()
        for n in range(len(bounds)):
            # assign values to independent variables, within given bounds
            inputs = inputs + (random.uniform(bounds[n][0],bounds[n][1]),)
            
        # evaluate function using given inputs, unpacking the tuple
        # append function value to end of inputs tuple, so we know where it is
        inputs = inputs + (f(*inputs),)
        values.append(inputs)
    # find maximum value in current set of function evaluations
    old_max = values[0]
    
    for n in range(len(values)):
        if values[n][-1] >= old_max[-1]:
            new_max = values[n]
            #print(old_max)
        
    return new_max
    
#def new_bounds(point,bounds):
#        
#    new_bounds = ()
#    for n in range(len(bounds)):
#        delta_up = abs(point[n]-bounds[n][1])
#        delta_down = abs(point[n]-bounds[n][0])
#        delta = 1.0*min((delta_up),(delta_down))
#        new_bounds = new_bounds + (((point[n]-delta),(point[n]+delta)),)        
#    return new_bounds    

def optimize_md(f,bounds):
    import random
    import numpy as np
    #define a tolerance for comparing old/new max values
    tol = 1/10000
    #define a difference variable
    diff = 1
    #define first "maximum" value
    old_max = eval_func_rand(f,bounds,1000)    
    
    while diff >= tol:
        #use first maximum estimate to divide bounds into two sectors
        lower_bounds,upper_bounds = divide_bounds(bounds,old_max)
        #evaluate function within the two sectors
        lower_max = eval_func_rand(f,lower_bounds,1000)        
        upper_max = eval_func_rand(f,upper_bounds,1000)
        #test to see if new maximum values are greater/smaller than old value        
        if lower_max[-1] >= upper_max[-1] and lower_max[-1] >= old_max[-1]:
            old_max = lower_max
            diff = abs((lower_max[-1] - old_max[-1]))
        
        if upper_max[-1] >= lower_max[-1] and upper_max[-1] >= old_max[-1]: 
            old_max = upper_max            
            diff = abs((upper_max[-1] - old_max[-1]))        
        
    return old_max
        
if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    import numpy as np
    import random 
    from scipy import optimize
    
    
    # evaluate first function
    
    def f(x):        
        return -1*((x+2)**2) + 5
    
    #inverted function for fmin
    def g(x):
        return (x+2)**2 + 5
    
    bounds = (-3,12.4)
    steps = [10, 50, 100, 200, 500, 1000,2000]
    max_step =[]
    max_random = []
    
    #use built-in to find true minimum
    minimum = optimize.fmin(g,1,disp = False)
    
    for n in steps:
        step = optimize_step(f,bounds,n)
        max_step = np.append(max_step, step[0])
        rand = optimize_random(f,bounds,n)
        max_random = np.append( max_random, rand[0])
    
    x = np.linspace(bounds[0],bounds[1],1000)
    y = f(x)
    step_error = 100*abs((max_step-(minimum))/(minimum))
    random_error = 100*abs((max_random-(minimum))/(minimum))

    print('\n\ntesting 1-D function optimization: f(x) = -1*((x+2)**2) + 5')
    print('stepwise max @ x = ' + str(max_step[-1]))
    print('random max @ x = ' + str(max_random[-1]))    
    print('fmin result: ' + str(minimum))
    print('close figure for next result')
    
    plt.figure()    
    plt.plot(steps,step_error)
    plt.plot(steps,random_error)
    plt.axvline(x = 40,color='g')
    plt.legend(['uniform increment','random increment','fmin calls (40)'])
    plt.xlabel('number of evaluations')
    plt.ylabel('% error for estimated maximum value')
    plt.title('f = (x+2)^2 + 5')
    plt.show()
    
    # evaluate second function
    
    def f(x):        
        return -1*((x+4)**4 -4 )
    
    #inverted function for fmin
    def g(x):
        return ((x+4)**4 -4 )
    
    bounds = (-10,12.4)
    steps = [10, 50, 100, 200, 500, 1000,2000]
    max_step =[]
    max_random = []
    
    #use built-in to find true minimum
    minimum = optimize.fmin(g,1,disp = False) #
    
    for n in steps:
        step = optimize_step(f,bounds,n)
        max_step = np.append(max_step, step[0])
        rand = optimize_random(f,bounds,n)
        max_random = np.append( max_random, rand[0])
    
    x = np.linspace(bounds[0],bounds[1],1000)
    y = f(x)
    step_error = 100*abs((max_step-(minimum))/(minimum))
    random_error = 100*abs((max_random-(minimum))/(minimum))

    print('\n\ntesting 1-D function optimization: f(x) = -1*((x+4)**4 - 4 )')
    print('stepwise max @ x = ' + str(max_step[-1]))
    print('random max @ x = ' + str(max_random[-1]))    
    print('fmin result: ' + str(minimum))
    print('close figure for next result')
    
    plt.figure()    
    plt.plot(steps,step_error)
    plt.plot(steps,random_error)
    plt.axvline(x = 40,color='g')
    plt.legend(['uniform increment','random increment','fmin calls (42)'])
    plt.xlabel('number of evaluations')
    plt.ylabel('% error for estimated maximum value')
    plt.title('f(x) = -1*((x+4)**4 -4 )')
    plt.show()
    
    def f_md(x,y):
        return -(x**2)+y 
    
    bounds = ((1,2),(1,2))
    max_value = optimize_md(f_md,bounds)
    print('\n\ntesting multidimensional function optimization')
    print('estimated maximum: ' + str(max_value[-1]))
    print('true maximum: 1')
    print('pretty poor performance, if you ask me')
   

