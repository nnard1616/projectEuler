# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:54:44 2016

@author: Nathan
"""


import sys
import time
start_time = time.time()


sys.setrecursionlimit(1500)

def find_numerators1(n=3, d=2, c =0, i = 0):
    if len(str(n)) > len(str(d)):
        c+=1
        print c
    if i==1000:
        return 
    return find_numerators1(n+2*d, n+d, c, i+1)


#this will do it for sqrt(2)
#def convergents(n):
#    if n == 0:
#        return 2
#    return 1+ 1.0/(1+convergents(n-1))
    
find_numerators1()

print("--- %s seconds ---" % (time.time() - start_time))