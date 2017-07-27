# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 03:30:33 2016

@author: Nathan
"""


import time
start_time = time.time()


def is_palindrome(n):
    s = list(str(n))
    s.reverse()
    nr = int(''.join(s))
    if n == nr:
        return True
    else:
        return False
        
def find_palindrome (i, n, remNums): #i stands for iterations, n stands for number
    if i == 50:
        return None
    listN = list(str(n))
    listN.reverse()
    nr = int(''.join(listN))
    nextIter = n+nr
    if is_palindrome(nextIter):
        return remNums
    else:
        if nextIter < 10000:
            remNums.append(nextIter)
        return find_palindrome(i+1, nextIter, remNums)



result = find_palindrome(0, 349, [])
nums = range(5,10001)
lychrels = []
for num in nums:
    result = find_palindrome(0, num, [])
    if result == None:
        lychrels.append(num)
    else:
        for d in result:
            try: rem = nums.pop(nums.index(d))
            except: pass
print len(lychrels)

print("--- %s seconds ---" % (time.time() - start_time))