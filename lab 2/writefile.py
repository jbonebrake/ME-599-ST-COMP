# -*- coding: utf-8 -*-
#!usr/bin/env python 3

def write_file(data,filepath):
    with open(filepath,'w') as f:
        for n in data:
            f.write(str(n)+'\n')
        f.close()
