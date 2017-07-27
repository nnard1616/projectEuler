# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:39:54 2016

@author: Nathan
"""

import time
start_time = time.time()

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

#recursive version, computation time grows on n! time.
#def prime_partitions(n):
#    if n==1:
#        return 0
#    return (sum(set(prime_factors(n)))+ 
#            sum(map(lambda k: sum(set(prime_factors(k)))*prime_partitions(n-k), range(1,n))))/n
#    """ return (c_n + c_k*b_n-k)/n for k = 1, 2, ... , n-1
#        where c_n is the sum of the prime factors of n, and b_n is the prime partitions of n."""

b = {} #prime partitions of n stored here
c = {} #sum of prime factors of n stored here

b[1] = 0
c[1] = 0
def prime_partitions(n):
    prime_sum = sum(set(prime_factors(n)))
    c[n] = prime_sum
    b[n] = (c[n]+ sum(map(lambda k: c[k]*b[n-k], range(1,n))))/n
    """ b_n = (c_n + c_k*b_n-k)/n for k = 1, 2, ... , n-1
        where c_n is the sum of the prime factors of n, and b_n is the prime partitions of n."""
    return

n=1
while b[n] <= 5000:
    n+=1
    prime_partitions(n)
print n, b[n]
print("--- %s seconds ---" % (time.time() - start_time))
