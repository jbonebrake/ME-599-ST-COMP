# -*- coding: utf-8 -*-
#!usr/bin/env python 3


#NOTE: change input to "number_list"
def sum_i(numbers):
    total = 0
    for n in numbers:        
        total += n        
    return total
        
def sum_r(numbers):
    if len(numbers) ==0:
        #if the length of input list is 0, the list is empty, sum is 0 
        print('empty list')
        return 0
    elif len(numbers) == 1:
        #if the length of input list is 1, the "sum" is the only element 
        return numbers[0]
    else:
        #return the first element + function call for the all but last element
        #if the list numbers[:-1] is larger than 1 element, function recurses
        return numbers[-1] + sum_r(numbers[:-1])
    
    
if __name__ == '__main__':
    
    # tests compare function to numpy flip function
    import numpy as np
    input1_i = np.random.rand(np.random.randint(1,256))
    test1_i = sum_i(input1_i)
    
    if np.abs(test1_i - np.sum(input1_i)) <= 10**(-10):
        print('test passed for iterative function')
    else:
        print('test not passed for iterative function')
        print(np.abs(test1_i - np.sum(input1_i)))
        
    input1_r = np.random.rand(np.random.randint(1,256))
    test1_r = sum_r(input1_r)
    
    if np.abs(test1_r - np.sum(input1_r)) <= 10**(-10):
        print('test passed for recursive function')
    else:
        print('test not passed for recursive function')
        print(np.abs(test1_r - np.sum(input1_r)))
    
