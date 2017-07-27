# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:09:21 2016

@author: Nathan
"""

import time
from math import sqrt
start_time = time.time()

tri = lambda(x): x*(x+1)/2
pent = lambda(x): x*(3*x-1)/2
hexa = lambda(x): x*(2*x-1)

def is_pent(x):
	f = (.5 + sqrt(.25+6*x))/3
	return f.is_integer()

def is_hexa(x):
    f = (0.5 + sqrt(0.25+2*x))/2
    return f.is_integer()


for i in range(1,100001):
    if is_pent(tri(i)) and is_hexa(tri(i)):
        print tri(i)

print("--- %s seconds ---" % (time.time() - start_time))