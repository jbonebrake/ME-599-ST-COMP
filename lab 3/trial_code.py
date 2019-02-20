# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:29:52 2019

@author: jmich
"""

import time
import string

time_start = time.time()

#with open('war_and_peace.txt') as f:    
with open('test_file_1.txt') as f:    
    #read in words from file, line by line, splitting by whitespace
    text = [word for line in f for word in line.split()]
    
# create translator to eliminate punctuation
translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
# remove whitespaces from punctuation removal, make everything lowercase
text1_clean = [word.lower() for word in str(text).translate(translator).split() if word != ' ']
print(len(text1_clean))

#with open('words.txt') as f:
with open('test_file_2.txt') as f: 

    #read in words from file, line by line, splitting by whitespace
    text = [word for line in f for word in line.split()]
    
# remove whitespaces from punctuation removal, make everything lowercase
text2_clean = [word.lower() for word in str(text).translate(translator).split() if word != ' ']

print(len(text2_clean))

## Find unique elements
text1 = set(text1_clean)
text2 = set(text2_clean)

unique1 = list(text1-text2)
unique2 = list(text2-text1)

print(len(unique1))
print(len(unique2))


# find unique words in lists
seen1 = set()
uniq1 = []
for x in text1:
    if x not in seen1:
        uniq1.append(x)
        seen1.add(x)

seen2 = set()
uniq2 = []
for x in text2:
    if x not in seen2:
        uniq2.append(x)
        seen2.add(x)
        
print(len(uniq1))
print(len(uniq2))

time_end = time.time()
print(time_end-time_start)
