# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 20:58:02 2016

@author: Nathan
"""

import time
from fractions import Fraction
start_time = time.time()

    
def convergents(n,maxn):
    if n == 0 and maxn==0: #gate 1
        return Fraction(2,1)
    if n == 0 and (maxn-n)%3 == 1:
        return 2*(Fraction((maxn-n),3)+Fraction(2,3))
    if n == 0 and (maxn-n)%3 != 1:
        return 0
    if (maxn-n)%3 == 1:
        return (2*(Fraction((maxn-n),3)+Fraction(2,3))+convergents(n-1, maxn))**-1
    if maxn == n and n>1:
        return Fraction(2,1) + (1+ convergents(n-1, maxn))**-1
    if maxn == n and n==1:
        return Fraction(2,1) + (3 - convergents(n-1, maxn))**-1 #need the '3-' to remove the 2 from gate 1.  this gate only matters when calculating e for 1 iteration (yielding '3')
    if (maxn-n)%3 != 1:
        return (Fraction(1,1)+ convergents(n-1, maxn))**-1
        
lastc = convergents(99,99)
print sum(map(int, list(str(lastc.numerator))))

print("--- %s seconds ---" % (time.time() - start_time))