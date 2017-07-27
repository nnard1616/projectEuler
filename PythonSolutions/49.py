# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:46:06 2016

@author: Nathan
"""
import time
from itertools import permutations
start_time = time.time()

f = open("primes.txt", "r")
lines= f.readlines()
f.close()

primes = []


for line in lines:
    nums = []
    nums += line.split()
    for num in nums:  
        primes.append( int(num))

def cat_list_items(l):
    newL = []
    for item in l:
        newL.append(int(''.join(item)))
    return newL

for prime in primes:
    perms = list(permutations(str(prime)))
    perms = cat_list_items(perms)
    perms.sort()
    for perm in perms:
        if perm > prime: #prime is the current prime number in our list of primes.
            try:
                primes.index(perm) #if it works, then the permutation is another prime number
                d = perm - prime
                primes.index(perm+d)
                perms.index(perm+d)
                print prime, perm, perm+d
            except:
                pass










print("--- %s seconds ---" % (time.time() - start_time))
