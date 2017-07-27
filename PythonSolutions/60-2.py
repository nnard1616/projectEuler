# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 19:32:23 2016

@author: Nathan
"""
import time

def _isPrimeN(n):
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


_allprimes = []
maxPrime = 10000
for n in range(maxPrime+1):
    if _isPrimeN(n):
        _allprimes.append(n)

_allprimes.sort()   
    
    
    
def _dictprimes(nmax):
	st = time.time()
	st0 = st
	di = {}
	di[(3,)] = [7]
	di[(7,)] = [3]
	nb = 1
	tmp = _allprimes
	for pr in tmp:
		if pr<=7:
			continue
		nb+=1
		if not(nb%100):
			cu = time.time()
			print '--%4d/%4d--%3.2f--%3.2f--' %(nb/100,pr,cu-st,cu-st0)
			st = cu
		tmp = str(pr)
		for k in di.keys():
			if _isPrimeN(int(tmp+str(k[0]))):
				if _isPrimeN(int(str(k[0])+tmp)):
					di.setdefault(k,[]).append(pr)
					di.setdefault((pr,),[]).append(k[0])
				else:
					di[(pr,)] = []
	return di

def pb60a(nmax=10000):
	di = _dictprimes(nmax)
	clen = 1
	occ = 1
	while occ>0:
		occ = 0
		for k,v in di.items():
			if len(k)==clen:
				for vv in v:
					if vv>max(k):
						di[k+(vv,)]  = [x for x in di[(vv,)] if x in v]
						occ+=1
		clen += 1
		print 'Depth %d occurences %d' %(clen,occ)
	return di
 
d = pb60a()