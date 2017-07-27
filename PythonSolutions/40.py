# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 20:29:02 2016

@author: Nathan
"""
num = ""
for i in range(1,1000001):
    i = str(i)
    num+=i

print int(num[0])*int(num[9])*int(num[99])*int(num[999])*int(num[9999])*int(num[99999])*int(num[999999])