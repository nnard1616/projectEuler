# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 02:49:11 2016

@author: Nathan
"""

import math
import time
start_time = time.time()

def nCr(n,r):
    f = math.factorial
    return f(n)/f(n-r)/f(r)
    
minR = 3
s= 0

for n in range(100, 22, -1):
    r = minR
    while nCr(n,r) < 10**6:
        r+=1
    minR = r-1
    s += (n-2*r+1)
print  s
        



print("--- %s seconds ---" % (time.time() - start_time))