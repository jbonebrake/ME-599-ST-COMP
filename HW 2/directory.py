# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 HW 2
# Jonathan Bonebrake


# url for single word search: http://directory.oregonstate.edu/?type=search&cn=bonebrake
# url for multiple word search: http://directory.oregonstate.edu/?type=search&cn=carter+michael

class person():
    def __init__(self,name = 'none', title = 'none', department = 'none',\
                 phone = 'none'):   
        #initialize variables as 'none' in case data does not exist
        self.name = 'none'
        self.title = 'none'
        self.department = 'none'
        self.phone = 'none'

def osu_dir_search(name = 'john doe'):
    
    import string
    from urllib.request import urlopen
    
    print('searching for: ' + '"' + name + '"')
    #format input string for directory search
    translator = str.maketrans(' ', '+')
    search_name = name.translate(translator)
    search_url = 'http://directory.oregonstate.edu/?type=search&cn=' + search_name
    #perform directory search
    search = urlopen(search_url)
    search_result = str(search.read())
    
    return search_result

def chop(data,field):
    # return data after "field" 
    # use this functon to find the record of interest
    import string

    # check to see if multiple entries
    try:
        check = data.split('Found')
        num = check[1].split('</h2>')
        return num[0]
    
    except:
        data = data.split(field)
        
        try:
            return data[1]
        except:
            #print('whats wrong?')
            # if splitting into records does not work, look for an error
            try: 
                #print('look for error')
                error = data[0].split('Error:')
                #print(error[1])
                error_clean = error[1].split('</h2>')
                #print(error_clean[0])
                return error_clean[0]
            except:
                
                return str(' Entry not found')
            
        #return str('entry not found')

def create_person(id):
    # create person class from formatted data (tuples of: name,value)
    # leaves default values if none exist for keywords
    result = person()
    for entry in id:
        if entry[0] == 'Full Name':
            result.name = entry[1]
        if entry[0] == 'Title':
            result.title = entry[1]
        if entry[0] == 'Department':
            result.department = entry[1]
        if entry[0] == 'Office Phone Number':
            result.phone = entry[1]
    return result

def fix_phone(person):
    # reformat the phone number entry, which is a bit screwy from the web
    if person.phone == 'none':
        return person
    else: 
        phone_string = person.phone 
        phone_string = phone_string.split('>')
        phone = phone_string[1]
        phone = phone.replace('<a','')
        person.phone = phone
        return person
    
## line ##    
import sys

try:
    name = str(sys.argv[1] + ' ' + sys.argv[2])  

except:
    name = str(sys.argv[1])

# scrape the data
data = osu_dir_search(name)

# extract name, title, etc.
parsed = chop(data,'<div class="record">')

#deal with too many entries error
if parsed == ' Too many entries returned. Try a more precise search.':
    print('\n'+ 'Error:' + parsed)

if parsed == ' Entry not found':
    print('\n'+ 'Error:' + parsed)   
    
if 'matches' in parsed :
    print('\n'+ 'Error:' + parsed)   
    
# clean up the data and split into entries
replaced_split = parsed.replace("/",'').replace('<dt>','').replace('<dd>','').split('<b>')
chopped = replaced_split[1:-1]
#split data into name, title, etc. entries
entries = []        
for line in chopped:
    entries.append(line.replace("\\n",'').replace("\\t",'').strip())

# format data into list of tuples
n = 0
id = []    
while n < len(entries)-1:
    id.append((entries[n],entries[n+1]))
    n = n+2

# create person 
result = create_person(id)
# fix the phone number
result = fix_phone(result)

# test for results present, and print if present 
if result.name != 'none':
    print('\nName: ' + result.name)
    print('Title: ' + result.title)
    print('Department: ' + result.department)
    print('Phone: ' + result.phone)

    
#if __name__ == '__main__':
 
# Test for entry with all fields present    
##    name = 'david blunck'
# Test for given example    
#    name = 'edward feser'
# Test for too many entries
##    name = 'john smith'
# Test for no entries    
##    name = 'bill smart'
    
#    # pull data from website
#    data = osu_dir_search(name)
#    # extract name, title, etc.
#    # clean up the data and split into entries   
#    parsed = chop(data,'<div class="record">')
#    #deal with too many entries error
#    if parsed == ' Too many entries returned. Try a more precise search.':
#        print('\n'+ 'Error:' + parsed)
#    
#    if parsed == ' Entry not found':
#        print('\n'+ 'Error:' + parsed)   
#        
#    if 'matches' in parsed :
#        print('\n'+ 'Error:' + parsed)   
#
#    replaced_split = parsed.replace("/",'').replace('<dt>','').replace('<dd>','').split('<b>')
#    chopped = replaced_split[1:-1]
#    #split data into name, title, etc. entries
#    entries = []        
#    for line in chopped:
#        entries.append(line.replace("\\n",'').replace("\\t",'').strip())
#    
#    # format data into list of tuples
#    n = 0
#    id = []    
#    while n < len(entries)-1:
#        id.append((entries[n],entries[n+1]))
#        n = n+2
#    
#    result = create_person(id)
#
#        