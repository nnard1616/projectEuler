# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 02:55:10 2016

@author: Nathan
"""
import time
from math import sqrt
start_time = time.time()
#
#pentSums = []
#pentDiffs = []
#
#class pent_pair:
#    def __init__(self, m, n): # n>m
#        self.m = m
#        self.n = n
#
#
#def pent_formula(n):
#    return n*(3*n-1)/2
#    
#
#for m in range(1,10001):
#    k = 1
#    while k < m/3.0: #for finding sum pents
#        n = (m**2-k-9*k**2+6*k*m-m**2)/(2.0*m-6*k)
#        if n > m and n.is_integer():
#            pentSums.append(pent_pair(pent_formula(m), pent_formula(n)))
##            break
#            k+=1
#        else:
#            k+=1
#    k = 1
#    while k < m/3.0: #for finding diff pents
#        n = (-2*m**2+k-9*k**2+6*k*m)/(6*k-2.0*m)
#        if n > m and n.is_integer():
#            pentDiffs.append(pent_pair(pent_formula(m), pent_formula(n)))
##            break
#            k+=1
#        else:
#            k+=1
#
#for x in pentSums:
#    for y in pentDiffs:
#        if x.m == y.m and x.n == y.n:
#            print x.m, x.n
#            print("--- %s seconds ---" % (time.time() - start_time))
pent = lambda(x): x*(3*x-1)/2
def is_pent(x):
	f = (.5 + sqrt(.25+6*x))/3
	if f - int(f) == 0:
		return True
	else:
		return False

flag = False
for i in range(1,3000):
	if i % 100 == 0:
		print 'i = %d' % i 
	for j in range(i+1,3000):
		if is_pent(pent(j) - pent(i)) and is_pent(pent(j) + pent(i)):
			print 'answer = %d' % (pent(j) - pent(i))
			flag = True
			break
	if flag:
		break

print("--- %s seconds ---" % (time.time() - start_time))