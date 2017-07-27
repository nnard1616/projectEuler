# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 02:05:38 2016

@author: Nathan
"""
from itertools import permutations

panSum = 0

def is_pandigital(n):
    digits = []
    for c in str(n): digits.append(int(c))
    digits.sort()
    if digits == range(10):
        return 1
    else:
        return 0
        
primes = [2,3,5,7,11,13,17]

for num in permutations('0123456789', 10):
    if num[0] != '0':
        num = int(''.join(num))
        if is_pandigital(num):
            num = str(num)
            if int(num[1:4]) % 2 == 0:
                if int(num[2:5]) % 3 == 0:
                    if int(num[3:6]) % 5 == 0:
                        if int(num[4:7]) % 7 == 0:
                            if int(num[5:8]) % 11 == 0:
                                if int(num[6:9]) % 13 == 0:
                                    if int(num[7:]) % 17 == 0:
                                        panSum += int(num)

print panSum