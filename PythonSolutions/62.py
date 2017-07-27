# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:50:59 2016

@author: Nathan
"""

import time
#import itertools
#from math import factorial as f
start_time = time.time()

cubes = []
for n in range(11,10000):
    cubes.append(n**3)

for c1 in cubes:
    digits1 = list(str(c1))
    digits1.sort()
    common = [c1]
    for c2 in cubes[cubes.index(c1)+1:]:
        digits2 = list(str(c2))
        digits2.sort()
        if digits1 == digits2:
            common.append(c2)
        if len(digits2) > len(digits1):
            break
    if len(common) == 5:
        print common
        break


print("--- %s seconds ---" % (time.time() - start_time))