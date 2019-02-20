# -*- coding: utf-8 -*-
#!usr/bin/env python 3
"""
Created on Wed Jan 23 11:20:54 2019

@author: jbonebrake
"""
#checks: int, odd, <len(data), >0, is num
# add shebang

def mean_filter(data,*width):
    # check if filter width specified, if not, set to 3
    if len(width) == 0:
        f_width = 3
    # set filter width variable    
    elif len(width) != 0:
        f_width = width[0]
        #width = width[0]
        #print(type(f_width))
    # check if filter width is int    
    if type(f_width) == int:   
        #check if filter width is odd
        if f_width % 2 == 1:
            #check if filter width == 1
            if f_width != 1:
                #check if filter width is <= # of data elements
                if f_width <= len(data):
                    # check that data to be filtered is correct type
                    if type(data) == list:
                        # check that enough data was provided 
                        if len(data) >= 3:
                            from sum import sum_r
                            filtered = []
                            #calculate offset for start of loop to accomodate filter width
                            offset = (f_width-1)/2
                            for n in range(int(offset),int(len(data)-offset)):    
                                #calculate upper and lower indices for filter 
                                lower = int(n-(f_width-1)/2)
                                upper = int(n+1+(f_width-1)/2)
                                #calculate filtered element
                                filtered = filtered + [sum_r(data[lower:upper])/f_width]                                  
                            return filtered                            
                        else:
                            raise ValueError('1. data to be filtered must have at least 3 elements')
                    else:
                        raise ValueError('2. data to be filtered must be list')
                else:
                    raise ValueError('3. filter width must be less <= number of data elements')
            else: 
                raise ValueError('4. filter width must be odd integer greater than one')
        else: 
            raise ValueError('5. filter width must be odd integer greater than one')
    else:
        raise ValueError('6. filter width must be odd integer greater than one')

if __name__ == '__main__':

    data = [1,2,3,2,1,2,3,2,1,2,3,2,1]
    
    check = mean_filter(data)
    if check == [2, 7/3, 2, 5/3, 2, 7/3, 2, 5/3, 2, 7/3,2]:
        print('test 1 passed for mean_filter')
    else:
        print('test 1 failed for mean_filter')
    
    check = mean_filter(data,5)
    if check == [9/5,2,11/5,2,9/5,2,11/5,2,9/5]:
        print('test 2 passed for mean_filter')
    else:
        print('test 2 failed for mean_filter')
            
        