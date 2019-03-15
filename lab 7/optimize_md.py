# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:23:01 2019

@author: jmich
"""

def divide_bounds(bounds,point):
    #calculate new bounds above and below given point
    upper_bounds = ()
    lower_bounds = ()   
    for n in range(len(bounds)):        
        upper_bounds = upper_bounds + ((point[n],bounds[n][1]),)
        lower_bounds = lower_bounds + ((bounds[n][0],point[n]),)        
    return lower_bounds,upper_bounds    

def eval_func_rand(f,bounds,n_eval):
    # evaluate function randomly within bounds, return maximum value
    import random
    values = list()
    for i in range(n_eval):
        inputs = ()
        for n in range(len(bounds)):
            inputs = inputs + (random.uniform(bounds[n][0],bounds[n][1]),)
            
        #append function value to end of inputs tuple, so we know where it is
        inputs = inputs + (f(*inputs),)
        values.append(inputs)
    # find maximum value
    new_max = values[0]
    for n in range(len(values)):
        if values[n][-1] >= old_max[-1]:
            new_max = values[n]
            #print(old_max)
        
    return new_max
    
def new_bounds(point,bounds):
        
    new_bounds = ()
    for n in range(len(bounds)):
        delta_up = abs(point[n]-bounds[n][1])
        delta_down = abs(point[n]-bounds[n][0])
        delta = 1.0*min((delta_up),(delta_down))
        new_bounds = new_bounds + (((point[n]-delta),(point[n]+delta)),)        
    return new_bounds    

def optimize_md(f,bounds):
    import random
    import numpy as np
    #n_eval = 100
    tol = 1/10000
    diff = 1
    old_max = eval_func_rand(f,bounds,1000)    
    
    while diff >= tol:
        lower_bounds,upper_bounds = divide_bounds(bounds,old_max)
        lower_max = eval_func_rand(f,lower_bounds,1000)
        
        upper_max = eval_func_rand(f,upper_bounds,1000)
                
        if lower_max[-1] >= upper_max[-1] and lower_max[-1] >= old_max[-1]: #\
        #and (lower_max[-1] - old_max[-1]) >= tol:
            old_max = lower_max
            
            diff = (lower_max[-1] - old_max[-1])
        
        if upper_max[-1] >= lower_max[-1] and upper_max[-1] >= old_max[-1]: #\
        #and (upper_max[-1] - old_max[-1]) >= tol:
            new_max = upper_max
            
            diff = (upper_max[-1] - old_max[-1])        
        
        else:
            diff = tol
                
        return old_max
        
    return new_max


if __name__ == '__main__':
    
    def f(x,y):
        return -(x**2)+y 
    
    bounds = ((1,2),(1,2))
    max_value = optimize_md(f,bounds)
    print('testing multidimensional function optimization')
    print('estimated maximum: ' + str(max_value[-1]))