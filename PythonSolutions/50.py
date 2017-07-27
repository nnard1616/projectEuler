# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:56:21 2016

@author: Nathan
"""

import time
start_time = time.time()

f = open('100000.txt', 'r')
lines = f.readlines()
f.close()

maxSum = 1000000
primes = []
for line in lines:
    nums = []
    nums += line.split()
    for num in nums: 
        if int(num) < maxSum:
           primes.append( int(num))
        else:
           break

c = 0
while sum(primes[:c])< maxSum:
    c+=1
c -= 1
#c is the max end index that will yield a possible sum  less than 1000000
    
    
milestones = []
t = (0,546) #first range of consecutive primes that sum to just below 1000000
milestones.append(t)
b = 0
while (c-b) > 100: # generates more ranges of consecutive primes's indeces that sum to just below 1000000
    s=0
    for p in reversed(primes[:c]):
        if s < 10**6:
            s+=p
        else:
            milestones.append((primes.index(p)+2, c))
            b = primes.index(p)+2
            break
    c+=1


currMaxLength = 21
currMaxSum = 953
for pair in milestones:
    b = pair[0]
    c = pair[1]
    if c-b < currMaxLength:
        break
    while b != c:
        try:
            s = sum(primes[b:c])
            l = len(primes[b:c])
            primes.index(s)
            if l > currMaxLength:
                currMaxSum = s
                currMaxLength = l
        except:
            pass
        b+=1
    

print currMaxLength, currMaxSum

print("--- %s seconds ---" % (time.time() - start_time))