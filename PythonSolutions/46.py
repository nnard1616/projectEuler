# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:32:15 2016

@author: Nathan
"""
import time
from math import sqrt
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
    
for i in range(9,10002,2):
    if not is_prime(i):
        x=1
        switch = False
        while x <= sqrt((i-2)/2):
            if is_prime(i-2*x**2):
                switch = True #the number satisfies GOC
                break
            x+=1
        if switch == False: #the number is composite and does not satisfy GOC
            print i
            break
                
            
print("--- %s seconds ---" % (time.time() - start_time))