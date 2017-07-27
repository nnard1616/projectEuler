# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 19:39:15 2016

@author: Nathan
"""
import time
import math
from fractions import Fraction
start_time = time.time()


def isprime(n):
    """Returns True if n is prime."""
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
    
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n%i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def no_common_factors(a, b):
    afacts = set(prime_factors(a))
    bfacts = set(prime_factors(b))
    if afacts.intersection(bfacts) == set():
        return True
    return False
    
def phi(n):
    product = n
    for p in set(prime_factors(n)):
        product *= (1-1.0/p)
    return product
    
def p71():
    poss = []
    
    for n in range(10**6, 4, -1):
        start = int((3/7.0)*n)
        while 1:
            if no_common_factors(start, n):
                poss.append(Fraction(start, n))
                break
            start -=1
    
    maxN = 0
    maxRatio = 0
    for p in poss:
        if p> maxRatio and p < Fraction(3,7):
            maxRatio = p
            maxN = p.numerator
            
    return maxRatio
    
def p72():
    uniques = 0
    for d in range(2,(10**6)+1):
        uniques += int(phi(d))
    return uniques
    
    
def p73():
    stuffs = []
    for d in range(5,12001):
        for n in range(d/3+1, d/2+1):
            if float(n)/d < 0.5:
                stuffs.append(float(n)/d)
    return len(set(stuffs))
        
#    return len(set([float(a)/b for a in xrange(1,12001) for b in range(a+1,12001) if float(a)/b > 1.0/3 if float(a)/b < .5 ]))
    
print p73()
pred = 0
for d in range(2,12001):
    pred += phi(d)
print pred/6.0
print("--- %s seconds ---" % (time.time() - start_time))
    