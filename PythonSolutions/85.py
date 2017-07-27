# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:45:35 2016

@author: Nathan
"""

import time
start_time = time.time()


tH = 0
tL = 0
tsum = 0
target = 2000000
s=0
sums = []
for H in range(1, 100):
    L = H
    s = 0
    while s < target:
#        s=0  #my algo, not so good
#        for h in range(1, H+1):
#            for l in range(1, L+1):
#                s+= ((H-h)+1)*((L-l)+1)
        s = H*(H+1)*L*(L+1)/4  #better algo
        if abs(target-s) < abs(target-tsum):
            tH = H
            tL = L
            tsum = s
            
        L += 1
        sums.append(s)
print tsum, tH, tL, tH*tL

#
#H = 36
#L = 77
#s=0
#for h in range(1, H+1):
#    for l in range(1, L+1):
#        s+= ((H-h)+1)*((L-l)+1)
#
#print s


print("--- %s seconds ---" % (time.time() - start_time))