# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:55:41 2016

@author: Nathan
"""
import time
start_time = time.time()

s = 0
for i in range(1,1001):
    c=0
    p = 1
    while c < i:
        p*=i
        c+=1
        if len(str(p))>10:
            p = int(str(p)[-10:])
    if len(str(p)) > 10:
        s+=int(str(p)[-10:])
    else:
        s+=p

print int(str(s)[-10:])