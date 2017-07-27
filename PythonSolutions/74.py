# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 15:17:13 2016

@author: Nathan
"""

import time, math
start_time = time.time()

def factSum(n):
    digits = map(int, list(str(n)))
    
    fSum = 0
    for d in digits:
        fSum += math.factorial(d)
    return fSum
    
def makeChain(chain):
    nextNum = factSum(chain[-1])
    try:
        chain.index(nextNum)
        return chain
    except:
        chain.append(nextNum)
        return makeChain(chain)

counter = 0
for n in range(0,1000000):
    if n%100000 == 0 :
        print n
    if len(makeChain([n])) == 60:
        counter+=1
print counter












print("--- %s seconds ---" % (time.time() - start_time))