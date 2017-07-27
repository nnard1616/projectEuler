# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:06:42 2016

@author: Nathan
"""

import time
start_time = time.time()

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n ** 0.5) # square root of n
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
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

def phi(n):
    product = n
    for p in list(set(prime_factors(n))):
        product *= (1-1.0/p)
    return product

    
def p69():
    maxRatio = 0
    maxN = 0
    for n in range(2,1000001):
        ratio = n/phi(n)
        if ratio > maxRatio:
            maxRatio = ratio
            maxN = n
    return maxN
#gets the answer but at 13 min of runtime
def p70():
    minRatio = 10**7
    minN = 10**7
    for n in range(2,10**7):
        if n%100000 == 0:
            print n
        p = int(phi(n))
        a = list(str(n))
        b = list(str(p))
        a.sort()
        b.sort()
        if a == b:
            ratio = float(n)/p
            if ratio < minRatio:
                minRatio = ratio
                minN = n
                
    return minN
    

#better attempt
def p70_1():
    start = (10**3.5)
    minRatio = 10**7
    minN = minRatio
    for x in range(int(start), 4000):
        for y in range(int(start), 2000, -1):
            if is_prime(x) and is_prime(y):
                n = x*y
                if n < 10**7:
                    p = int(phi(n))
                    
                    a = list(str(n))
                    b = list(str(p))
                    a.sort()
                    b.sort()
                    if a == b:
                        ratio = float(n)/p
                        if ratio < minRatio:
                            minRatio = ratio
                            minN = n
    return minN
print p70_1()
print("--- %s seconds ---" % (time.time() - start_time))