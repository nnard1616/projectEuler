# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:39:54 2016

@author: Nathan
"""

import time
start_time = time.time()
p = {}
p[-1] = 0
p[0] = 1

def partitions(n):#euler's implementation
	s = 0
	for k in range(1, int(n+1)):
		n1 = int(n-0.5*k*(3*k-1))
		n2 = int(n-0.5*k*(3*k+1))
		if n1 < 0:
			n1 = -1
		if n2 < 0:
			n2 = -1
		s+= ((-1)**(k+1))*(p[n1] + p[n2])
		
	p[n] = s
	return


for n in range(1,101):
	if n%10 == 0:
		print n
	partitions(n)

print p[100]
print("--- %s seconds ---" % (time.time() - start_time))
