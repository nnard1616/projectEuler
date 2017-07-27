# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:35:50 2016

@author: Nathan
"""

import time
start_time = time.time()

def are_permutes(n1, n2):
    digits1 = []
    for d in str(n1):
        digits1.append(d)
    for d in str(n2):
        try: digits1.pop(digits1.index(d))
        except: return False
    return True

#sNums = [16,166,1666,16666,166666,1666666,16666666,166666666,1666666666]
#done = False
#for num in sNums:
#    index = sNums.index(num)
#    while num > 10**(index+1) and not done:
#        for m in range(2,7):
#            if are_permutes(num, m*num): 
#                done = True
#            else: 
#                done = False
#                break
#        num -= 1
#    if done: 
#        print num+1
#        break


def permutatedmults(maximum):
    for i in range(100000, maximum):
        x2 = 2 * i
        x3 = 3 * i
        x4 = 4 * i
        x5 = 5 * i
        x6 = 6 * i
        if all(x in str(i) for x in str(x2)):
            if all(x in str(i) for x in str(x3)):
                if all(x in str(i) for x in str(x4)):
                    if all(x in str(i) for x in str(x5)):
                        if all(x in str(i) for x in str(x6)):
                            return i

print(permutatedmults(999999))







print("--- %s seconds ---" % (time.time() - start_time))