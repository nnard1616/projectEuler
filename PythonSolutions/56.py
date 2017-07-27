# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 04:39:30 2016

@author: Nathan
"""


import time
start_time = time.time()

smax = 0


            
print max(map(lambda n: sum(map(lambda d: int(d), list(str(n)))), [a**b for a in range(100) for b in range(100)]))
            

#        p = a**b
#        s = 0
#        for d in str(p):
#            s+=int(d)
#        smax = max(smax, s)
print smax

print("--- %s seconds ---" % (time.time() - start_time))