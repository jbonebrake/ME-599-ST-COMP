# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 HW 2
# Jonathan Bonebrake


# url for single word search: http://directory.oregonstate.edu/?type=search&cn=bonebrake
# url for multiple word search: http://directory.oregonstate.edu/?type=search&cn=carter+michael

class person():
    def __init__(self,name = 'none', title = 'none', department = 'none',\
                 phone = 'none'):   
        # default values for real ad imaginary parts are zero
        self.name = name
        self.title = title
        self.department = department
        self.phone = phone
    
        #to be added:
        #self.repr()
        #self.print()

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

def parse_result(data,field):
    # look for name, title, department, phone
    
    #name="cn" id="cn" value="jonathan bonebrake"
    import string
    
    data = data.split(field)
    return data[1]
 
if __name__ == '__main__':
    
    name = 'jonathan bonebrake'
    data = osu_dir_search(name)
    parsed = parse_result(data,'<div class="record">')
    
    rem_f_slash = str.maketrans('a','a','/')
    parsed = parsed.translate(rem_f_slash)
    