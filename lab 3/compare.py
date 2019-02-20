# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 lab 3
# Jonathan Bonebrake

import sys

# check number of inputs
if len(sys.argv) < 3 or len(sys.argv) > 3:
    print('compare requires two inputs and you supplied ' + str(len(sys.argv)-1))
    exit()

def unique_words(data):
    # find unique words in lists or sets
    seen = set()
    unique = []
    for word in data:
        if word not in seen:
            unique.append(word)
            seen.add(word)
    return unique

# create translator to eliminate punctuation
import string
translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))

# deal with first file
print(sys.argv[1])
with open(sys.argv[1]) as f:    
    #read in words from file, line by line, splitting by whitespace
    text1 = [word for line in f for word in line.split()]
    
# remove whitespaces from punctuation removal, make everything lowercase
text1_clean = [word.lower() for word in str(text1).translate(translator).split() if word != ' ']
print(str(len(text1_clean))+ ' words')
unique1 = unique_words(text1_clean)
print('unique: ' + str(len(unique1)))

# deal with second file
print(sys.argv[2])
with open(sys.argv[2]) as f:    
    #read in words from file, line by line, splitting by whitespace, list comprehensions are fantastic
    text2 = [word for line in f for word in line.split()]
    
# remove whitespaces from punctuation removal step, make everything lowercase
text2_clean = [word.lower() for word in str(text2).translate(translator).split() if word != ' ']
print(str(len(text2_clean))+ ' words')
unique2 = unique_words(text2_clean)
print('unique: ' + str(len(unique2)))

# Find unique words exclusive to each input, use "set" type for speed
exclusive1 = list(set(unique1)-set(unique2))
exclusive2 = list(set(unique2)-set(unique1))

print('Only ' + sys.argv[1] + ': ' + str(len(exclusive1)))
print('Only ' + sys.argv[2] + ': ' + str(len(exclusive2)))
print('Both files: ' + str(len(unique1)-len(exclusive1)))

