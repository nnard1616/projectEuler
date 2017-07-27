# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:57:22 2016

@author: Nathan
"""

import time
start_time = time.time()
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def factor_pairs(n):
    sets = []
    for f in range(int(n**0.5), 1, -1):
        if n%f ==0:
            sets.append([f, n/f])
    return sets


def factor_sets(n):
    sets = factor_pairs(n)
    
    for s in sets:
        if int((s[-1])**0.5) >= s[-2]:
            if len(primes(s[-1])) > 1:
                for pair in factor_pairs(s[-1]):
                    if pair[1] >= pair[0] and pair[0] >= s[-2]:
                        sets.append(s[0:-1]+pair)
                    else:
                        break
        if len(sets[-1]) == len(primes(n)):
            break
    return sets


def mps(k):
    maxmps = 2*k
    minmps = k
    if minmps < 4:
        minmps = 4
    domain = range(minmps, maxmps+1)
    for p in domain:
        parts = factor_sets(p)
        for part in parts:
            if p == sum([k-len(part)] + part):
                return p

mpsSet = set()
for k in range(2, 12001):
    newmps = mps(k)
    mpsSet.add(newmps)
    
print sum(list(mpsSet))


print("--- %s seconds ---" % (time.time() - start_time))
