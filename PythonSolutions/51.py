# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:23:11 2016

@author: Nathan
"""

import time
start_time = time.time()

f = open('100000.txt', 'r') #load text file of primes
lines = f.readlines()
f.close()

maxNum = 1000000 #going to make list of primes between 100000 and 1000000, saved as primes
minNum = 100000
primes = []
for line in lines:
    nums = []
    nums += line.split()
    for num in nums: 
        if int(num) < maxNum and int(num)> minNum:
            primes.append( num)
       
for p in primes: #primes is list of primes between 100000 and 1000000
    pSet = [] #list of primes in this prime cycle
    miss = 0 #non-prime counter
    for d in range(10): #cycle through replacing all instances of '1' in the current prime number with each number between 0 and 9.
        newP = p.replace("1", str(d)) 
        try: pSet.append(primes.pop(primes.index(newP))) #try moving replaced prime from primes list to pSet list.
        except: miss+=1 # if it didn't work, the replaced prime is not actually prime.
        if miss >2: break #if there's more than 2 non-prime numbers in this cycle of numbers, then move on to the next prime number
    if len(pSet) == 8:
        print pSet
        break
            
       
       
       
       
       
       
       
       
       
       
       
print("--- %s seconds ---" % (time.time() - start_time))