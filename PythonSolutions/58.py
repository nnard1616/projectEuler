# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 19:14:18 2016

@author: Nathan
"""

import time
start_time = time.time()

def isprime(n):
    """Returns True if n is prime."""
    if n ==1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True  
       
n=1
s = 1
diagList= [1]
p = 0.0

while p==0 or p/len(diagList)>=0.1:
    s+=2
    newDiags = range(n+(s-1), n+(s-1)*4+1, s-1)
    diagList+=newDiags
    for diag in newDiags:
        if isprime(diag):
            p+=1
        else:
            pass
    n = diagList[-1]
    if (s-1)%100 ==0: print s, p, len(diagList), p/len(diagList)


print diagList[-1], s
print("--- %s seconds ---" % (time.time() - start_time))