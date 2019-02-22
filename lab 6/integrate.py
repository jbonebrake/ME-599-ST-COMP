# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 6
# Jonathan Bonebrake

def integrate(f,a,b,n = 'default'):
    #integrate using Reimann sum
    # f = function (symbolic)
    # a = lower bound of integral
    # b = upper bound of integral
    # n = number of elements to sum
    
    if n == 'default':
        n = 1000
        
    import numpy
    from numpy import cos, sin, sqrt, pi, linspace, append
    x_values = linspace(a,b,n)
    w = (b-a)/n
    
    # define x and y-values, and perform reimann sum
    y_values = []
    rsum = []
    
    for x in x_values:
        y_values = append(y_values,eval(f))
 
    for y in range(len(y_values)):
        rsum = append(rsum,w*y_values[y])       
    
    integral = sum(rsum)
    
    return integral


def integrate_mc(f,a,b,limits, n= 100000):
    
    import random
    from numpy import cos, sin, sqrt, pi, linspace, append
    
#    greater = 0
#    smaller = 0
    inside = 0
    
    for m in range(n):
        x = random.randint(a,b)
        y = random.randint(limits[0],limits[1])
        
        if y < eval(f):
            inside = inside + 1
#        if y < eval(f):
#            smaller = smaller + 1
            
    integral = (b-a)*(limits[1]-limits[0])*inside/n
    
    return integral
        
        
        

if __name__ == '__main__':
    
    import numpy as np
    
    f = 'x**2'
    a = 0
    b = 5
    n = 100000
    
#    integral_1 = integrate(f,a,b,n)
#    integral_2 = integrate_mc(f,a,b,(-1,26),n)
    
    
    points = [10,100,1000,10000,100000]
    true_value = 125/3
    integral_1 = []
    integral_2 = []
    
    for n in points:
        integral_1 = np.append(integral_1,integrate(f,a,b,n))
        integral_2 = np.append(integral_2,integrate_mc(f,a,b,(-1,26),n))
        
    error_1 = 100*abs(integral_2-true_value)/true_value
    error_2 = 100*abs(integral_2-true_value)/true_value
    

    
    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(points,error_1)
    plt.plot(points,error_2)
    plt.legend('reimann','montecarlo')
    plt.xlabel('number of elements')
    plt.ylabel('absolute % error')
    plt.title('integral of: ' + f)