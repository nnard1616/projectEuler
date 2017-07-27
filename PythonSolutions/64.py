# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:42:53 2016

@author: Nathan
"""

import time
import math
import numpy
from fractions import gcd
import itertools
start_time = time.time()

######my solution
#counter = 0
#for n in range(2,10001):
#    if n**0.5 == round(n**0.5, 5):
#        print n
#        continue
#    numerator = 1.0
#    rp = math.floor(n**0.5)
#    denominator = n**0.5 - rp
#    
#    fraction = numerator/denominator
#    sequence = [fraction]
#    
#    denominator *= (n**0.5+rp)
#    denominator = round(denominator)
#    gFactor = gcd(numerator,denominator)
#    denominator /= gFactor
#    
#    numerator /= gFactor
#    numerator *= (n**0.5+rp)
#    numerator -= (denominator*math.floor(fraction))
#    rp  -= (denominator*math.floor(fraction))
#    rp*= -1
#    
#    nn = numerator
#    dd = denominator
#    
#    numerator = dd
#    denominator = nn
#    fraction = numerator/denominator
#    sequence.append(fraction)
#    while not numpy.isclose(sequence[0], sequence[-1]):
#        denominator *= (n**0.5+rp)
#        denominator = round(denominator)
#        gFactor = gcd(numerator,denominator)
#        denominator /= gFactor
#        
#        numerator /= gFactor
#        numerator *= (n**0.5+rp)
#        numerator -= (denominator*math.floor(fraction))
#        rp  -= (denominator*math.floor(fraction))
#        rp*= -1
#        
#        nn = numerator
#        dd = denominator
#        
#        numerator = dd
#        denominator = nn
#        
#        fraction = numerator/denominator
#        sequence.append(fraction)
#
#    if (len(sequence)-1) % 2 != 0:
#        counter +=1
#
#print counter


#best solution
def cf_period(r):
    p = int(math.sqrt(r))   # floor of sqrt(r)
    if p*p == r: return 0   # Square number
    q=1
    remainders = {}

    for pos in itertools.count(1):
        q=(r-(p*p))/q
        floor=int((math.sqrt(r)+p) /float(q))
        p = -1* (p- (floor*q))
        if (p,q) in remainders:
            return pos-remainders[p,q]
        remainders[p,q] = pos

print len([x for x in range(2,10001) if cf_period(x)%2==1])
print("--- %s seconds ---" % (time.time() - start_time))