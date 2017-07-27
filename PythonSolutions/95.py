# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 01:44:53 2016

@author: Nathan
"""
#super slow, but would probably be a lot faster in c++
import time

start_time = time.time()
memory = dict(zip(range(1000000), [0]*1000000))
maxChain = []
def factors(n):
    sets = []
    for f in range(1, int((n)**0.5)+1):
        if n%f ==0:
            sets.append(f)
            sets.append(n/f)
    sets.sort()
    sets.pop(-1)
    return sets

for n in range(2, 1000000):
    if n%100000 == 0:
        print n
    if memory[n] == 0:
        facts = factors(n)
        chain = [n]
        is_chain = False
        factsum = 0
        while len(facts) > 1 and factsum < 1000000:
            factsum = sum(facts)
            chain.append(factsum)
            facts = factors(factsum)
            if chain.count(factsum) >1:
                is_chain = True
                chain.pop(-1)
                first = chain.index(factsum)
                if first != 0:
                    chain = chain[first:]
                if len(chain) > len(maxChain):
                    maxChain = chain
                break
        if is_chain:
            for num in chain:
                memory[num] = chain[0]

values = list(memory.itervalues())
print len(values)          
print("--- %s seconds ---" % (time.time() - start_time))