# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 01:12:44 2016

@author: Nathan
"""
import string

a = string.ascii_uppercase
alpha = []
for c in a: alpha.append((c))

d = dict(zip(alpha, range(1,27)))

def word2num(word):
    s = 0
    for c in word: s+=d[c]
    return s
        
f = open("p042_words.txt", "r")
lines = f.readlines()
lines = lines[0].replace('"', "")
words = lines.split(',')


nums = []
for word in words:
    num = word2num(word)
    nums.append(num)

tris = []
for n in range(1, 21):
    tris.append(0.5*n*(n+1))
    
t = 0
for num in nums:
    try:
        tris.index(num)
        t+=1
    except:
        pass
    
print t

    
    