# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:21:06 2016

@author: Nathan
"""
import time
start_time = time.time()

def gcd(a, b):
    if (a%b == 0):
        return b
    else:
        return gcd(b, a%b)
        
def is_prime(n):
    if n==1:
        return False
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
#    
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

def clean_up(n, f):
    truncated = []
    for factor in f:
        if n%factor == 0:
            truncated.append(int(factor))
            n = n/factor
    truncated.sort()
    return truncated

def remove_dups(l):
    con = [] #consolidated list
    for item in l:
        try:  con.index(item)
        except: con.append(item)
    return con
        

#print is_prime(641)
c = 0
for i in range(640, 1000001):
#    if i % 10 == 0:
#		print 'i = %d' % i 
    if len(remove_dups(prime_factors(i))) == 4:
        c+=1
        if c==4:
            print i-3, i-2, i-1, i
            break
    else:
        c = 0

print("--- %s seconds ---" % (time.time() - start_time))