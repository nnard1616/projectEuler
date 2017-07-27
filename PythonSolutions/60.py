# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 22:20:46 2016

@author: Nathan
"""
import itertools
import time


        
def isprime(n):
    """Returns True if n is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True  

def is_special(l): # This will determine if l list of numbers has the special property
    pairs = list(itertools.combinations(l, 2))
    clear = False
    for pair in pairs:
        fnum = str(pair[0])
        snum = str(pair[1])
        forward = int(fnum+snum)
        reverse = int(snum+fnum)
        if isprime(forward) and isprime(reverse):
            clear = True
        else:
            clear = False
            return clear  
    return clear

##################### Hint online said all primes would be <10000.
##################### Make list of all primes <10000
primes = []
maxPrime = 10000
for n in range(maxPrime+1):
    if isprime(n):
        primes.append(n)

primes.sort()
##############################################################################
##############################################################################
##################### This next block of code makes a hash table for each prime
##################### that has at least one other prime buddy that has the con-
##################### catenation property.  These primes are the 'keys' and are
##################### mapped to a list of primes that are eligible cat buddies.
##################### Each list for each key only contains those buddies that 
##################### are greater than the key value.  
#####################     Example: specialPairs[673] = [769,1117,...]  
##################### Even though 673 and 3 can make a pair, 3 is smaller so is
##################### not included in the list for 673.
specialPairs = dict()    #the hashtable
sortedKeys = []    #list of the keys, to be sorted.  Needs to be in numerical order.
for p1 in primes:
    for p2 in primes[primes.index(p1)+1:]:
        if is_special([p1,p2]):
            try:
                specialPairs[p1].append(p2)
            except:
                specialPairs[p1] = []
                sortedKeys.append(p1)
                specialPairs[p1].append(p2)  
sortedKeys.sort()
##############################################################################
##############################################################################
##################### Block of code below finds intersections between lists
##################### of buddies in the hashtable.  First finds intersection
##################### between two lists, then iterates through the common 
##################### buddies in that intersection to see if they have 
##################### buddies in their respective list in the hash table that 
##################### intersect with the two list intersection, inter12.  This
##################### creates the three list intersection, inter123.  This pro-
##################### cess is continued until 5 iters (k1,k2,k3,k4,k5) are gen-
##################### erated. Then the group of 5 are checked if they have the 
##################### special property.
start_time = time.time()
specialGroups = [] 
for k1 in sortedKeys:
    for k2 in sortedKeys[sortedKeys.index(k1)+1:]:
        c = [specialPairs[k1], specialPairs[k2]]
        inter12 = list(set(c[0]).intersection(*c))
        inter12.sort()
        for k3 in inter12:
            try:#k3 may not be a key in the hashtable, so we need a try/except
                d = [inter12, specialPairs[k3]]
            except:
                continue
            inter123 = list(set(d[0]).intersection(*d))
            inter123.sort()
            for k4 in inter123:
#                if is_special([k1,k2,k3,k4]):
#                    specialGroups.append([k1,k2,k3,k4])
##################### Commented code above used for getting groups of 4.
##################### Code below gets groups of 5.
            
                try:#k4 may not be a key in the hashtable, so we need a try/except
                    e = [inter123, specialPairs[k4]]
                except:
                    continue
                inter1234 = list(set(e[0]).intersection(*e))
                inter1234.sort()
                for k5 in inter1234:
                    if is_special([k1,k2,k3,k4,k5]):
                        specialGroups.append([k1,k2,k3,k4,k5])
##############################################################################
##############################################################################
##################### Now we find the minimum sum.  Turned out there was only 
##################### one group of 5: [13, 5197, 5701, 6733, 8389], sum=26033
minSum = 1000000000000
for group in specialGroups:
    if sum(group) < minSum:
        minSum = sum(group)
print minSum
    

print("--- %s seconds ---" % (time.time() - start_time))
