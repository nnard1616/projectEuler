# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 20:57:17 2016

@author: Nathan
"""

import time
import itertools
import math
from fractions import Fraction
start_time = time.time()
#Read wiki article on Pell's equation for more quicker algos
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
            inverseRemainders = {}
            sequence = []
            
            for k,v in remainders.items():
                inverseRemainders[v] = k
            
            pair = inverseRemainders[len(inverseRemainders)]
            sequence.append(int(pair[1]/((r)**0.5-pair[0])))
            for i in range(1,len(remainders)):
                pair = inverseRemainders[i]
                sequence.append(int(pair[1]/((r)**0.5-pair[0])))
            return sequence
        remainders[p,q] = pos
        
def square_root_approximation(number, iterations, maxIters, sequence=[]):
    if len(sequence)!=0:
        currentApproxFracFloor = sequence[((maxIters-iterations)%len(sequence))-1]
    if iterations == 0 and maxIters == 0:
        return Fraction( int(number**0.5),1)
    if iterations ==0 and maxIters >0:
        return Fraction( currentApproxFracFloor, 1)
    if iterations == maxIters and iterations !=0:
        sequence = cf_period(number)
        return Fraction(int(number**0.5), 1) +1/(square_root_approximation(number, iterations-1, maxIters, sequence))
    if iterations != maxIters and iterations !=0:
        return currentApproxFracFloor+ 1/(square_root_approximation(number, iterations-1, maxIters, sequence))

def find_d():
    
    maxX = 0
    maxD = 0
    for d in range(2,1001):
        if d**0.5 == int(d**0.5):
            continue
        x = 0
        y = 0
        i = 0
        while x**2-d*y**2 !=1:
            i+=1
            f = square_root_approximation(d, i, i)
            x = f.numerator
            y = f.denominator
        if x > maxX:
            maxX = x
            maxD = d
    return maxD

    
    
print find_d()

print("--- %s seconds ---" % (time.time() - start_time))