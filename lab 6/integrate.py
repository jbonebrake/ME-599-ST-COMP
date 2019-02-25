# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 6
# Jonathan Bonebrake

def integrate(f,a,b,n = 'default'):
    # integrate using Reimann sum
    # f = function (symbolic)
    # a = lower bound of integral
    # b = upper bound of integral
    # n = number of elements to sum

    import numpy
    from numpy import cos, sin, tan, sqrt, pi, linspace, append
         
    if n == 'default':
        n = 10000
        print('no value for number of elements given, using n = 10000')
           
    x_values = linspace(a,b,n)
    w = (b-a)/n
    y_values = []
            
    for x in x_values:
        y_values = append(y_values,w*eval(f)) 
    integral = sum(y_values)
        
    return integral


def integrate_mc(f,a,b,limits, n = 'default'):

    import random
    from numpy import cos, sin, tan, sqrt, pi, linspace, append
    
    if n == 'default':
        n = 10000
        print('no value for number of samples given, using n = 10000')
           
    
    class point():
        def __init__(self,x = 0, y = 0):           
            self.x = x
            self.y = y
            
    negp = 0 #points within negative area
    negn = 0 #points attempted for negative area
    posp = 0 #points within positive area
    posn = 0 #points attempted for positive area
    
    # divide bounding box into positive, negative regions
    if limits[0] < 0:
        neg_area = (b-a)*limits[0]
    else:
        neg_area = 0
    pos_area = (b-a)*(limits[1]-limits[0]) + neg_area

    for m in range(int(n)):

        test = point(random.uniform(a,b),random.uniform(limits[0],limits[1]))
        x = test.x
        fx = point(test.x,eval(f))

        if test.y < 0:
            negn += 1
            if test.y >= fx.y:
                negp += 1

        if test.y > 0:
            posn += 1
            if test.y <= fx.y:
                posp += 1
 
    integral = pos_area*posp/posn + neg_area*negp/negn
    return integral
    #return pos_area,posp,posn,neg_area,negp,negn
        
def approximate_pi(n = 'default'):
    import random
    import numpy as np
    
    if n == 'default':
        n = 10000
        print('no value for number of samples given, using n = 10000')
    
    radii = set()
    for m in range(int(n)):
        radii.add(np.sqrt((random.uniform(-1,1))**2 \
                                         + (random.uniform(-1,1))**2))    
                                             
    inside = [r for r in radii if r <= 1]
    pi = 4*len(inside)/n
    return pi
        
if __name__ == '__main__':
   
# Test pi estimate
 
    import matplotlib.pyplot as plt
    import numpy as np       
    import scipy.integrate as scipy_integ
    
    points = [10,100,1000,10000,100000]
    pi = []
    
    for n in points:
        pi = np.append(pi,approximate_pi(n))
        print('for ' + str(n) + ' points, pi = ' + str(pi[-1]))
    
    pi_error = 100*abs((pi-np.pi)/np.pi)
        
    plt.figure()
    plt.plot(points,pi_error)
    
    plt.xlabel('number of samples')
    plt.ylabel('absolute % error')
    plt.title('rejection sampling estimate of pi')
    
    plt.savefig('pi_error.png')
    
    print('plot of error in pi estimate (pi_error.png) located in working directory')

# Test integration methods
    
    f = '50 + (x**2)*cos(x)'
    
    a = -2
    b = 10
    
    def integrand(x):
        from numpy import cos, sin, tan, sqrt, pi, linspace, append
        return eval(f)
    
    true_value, error_est = scipy_integ.quad(integrand,a,b)
    
    points = [100,1000,10000,100000]
    integral_1 = [] # reimann sum integral
    integral_2 = [] # montecarlo integral
    limits = (-45,90)
    
    print('integrating: ' + f)
    for n in points:
        integral_1 = np.append(integral_1,integrate(f,a,b,int(n)))
        integral_2 = np.append(integral_2,integrate_mc(f,a,b,limits,int(n)))
    
    print('correct value of integrand: ' + str(true_value))
    
    error_1 = 100*abs((integral_1-true_value)/true_value)
    error_2 = 100*abs((integral_2-true_value)/true_value)
    
    
    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(points,error_1)
    plt.plot(points,error_2)
    plt.legend(['reimann','montecarlo'])
    plt.xlabel('number of elements or samples')
    plt.ylabel('absolute % error')
    plt.title('integral of: ' + f)
    plt.savefig('integration_error.png')
    
    print('plot of error in integral estimate (integral_error.png) located in working directory')