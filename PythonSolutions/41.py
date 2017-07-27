# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:06:56 2016

@author: Nathan
"""

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

def is_pandigital(n):
    digits = []
    for c in str(n): digits.append(int(c))
    digits.sort()
    if digits == range(1, len(digits)+1):
        return 1
    else:
        return 0
    
for i in range(7652413, 987654321, 2):
    if is_pandigital(i):
        if is_prime(i):
            print i