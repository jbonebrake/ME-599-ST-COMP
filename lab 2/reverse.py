# -*- coding: utf-8 -*-
#!usr/bin/env python 3
"""
Created on Tue Jan 22 10:39:55 2019

@author: jbonebrake
"""

def reverse_i(input):
    # deal with empty list
    if len(input) == 0:
        #print('empty list')
        return []
    else:
        # group all characters in input list into a string
        # this makes the function react properly to lists of mixed type data
        for n in range(len(input)):
            if n == 0:
                words = str(input[n])
            else:
                words = words +str(input[n])
        # reverse order of word
        i = len(words)-1        
        while i >= 0:
            if i == len(words)-1:
                    reverse = [words[i]]
            else:
                    reverse = reverse + [words[i]]
            i = i-1
        # change element type to float if number
        # this helps to maintain input/output type
        for r in range(len(reverse)):
            if reverse[r].isdigit():
                reverse[r] = float(reverse[r])            
        return reverse
        

def reverse_r(input):
    # deal with empty list
    if len(input) == 0:
        return []
    else:
        # group all characters in input list into a string
        # this makes the function react properly to lists of mixed type data
        for n in range(len(input)):
            if n == 0:
                words = str(input[n])
            else:
                words = words +str(input[n])
        # reverse order of word
        reverse = [words[-1]] + reverse_r(words[:-1])
    # change element type to float if number
    # this helps to maintain input/output type
    for r in range(len(reverse)):
        if str(reverse[r]).isdigit():
            reverse[r] = float(reverse[r])            
    return reverse

if __name__ == '__main__':
    
    # tests compare function to numpy flip function and hardcode string example
    # numpy flip does not handle strings as requested in the assignment, so
    # the test for string input is hardcoded
    import numpy as np
    input1_i = [1,2,3,4,5]
    input2_i = ['hello']
    test1_i = reverse_i(input1_i)
    test2_i = reverse_i(input2_i)
    
    if test1_i == list(np.flip(input1_i)):
        print('test 1 passed for iterative function')
    else:
        print('test 1 not passed for iterative function')
    
    if test2_i == ['o', 'l', 'l', 'e', 'h']:
        print('test 2 passed for iterative function')
    else:
        print('test 2 not passed for iterative function')
            
    input1_r = [1,2,3,4,5]
    input2_r = ['hello']
    test1_r = reverse_r(input1_r)
    test2_r = reverse_r(input2_r)
    
    if test1_r == list(np.flip(input1_r)):
        print('test 1 passed for recursive function')
    else:
        print('test 1 not passed for recursive function')
    
    if test2_r == ['o', 'l', 'l', 'e', 'h']:
        print('test 2 passed for recursive function')
    else:
        print('test 2 not passed for recursive function')  