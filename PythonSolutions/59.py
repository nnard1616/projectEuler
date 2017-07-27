# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 21:15:30 2016

@author: Nathan
"""

import time
start_time = time.time()

f = open("p059_cipher.txt", "r")
lines = f.readlines()
f.close()

encMess = map(lambda a: int(a), lines[0].split(","))

lets = range(97,123)#97 to 122 is ASCII for a-z
passes = []
for let1 in lets: 
    for let2 in lets: 
        for let3 in lets: 
            passes.append([let1,let2,let3]) #generates all possible 3 letter passes in ASCII

for pas in passes:
    fullPass = pas*400
    fullPass.append(pas[0]) # this line and previous line make the repeated pass to equal the length of the encoded message(length is 1201).
    decMess = map(lambda e, p: e^p, encMess, fullPass) #generates decoded message in ASCII
    chrMess = ''.join(map(lambda a: chr(a), decMess)) #generates the Alpha decoded message from the decoded ASCII message
    if chrMess.find(" the ") != -1: #I guessed that the correct password would be the only one to generate ' the ' in the message.
        s = 0
        for d in decMess: s+=d
        break
print s, pas
print("--- %s seconds ---" % (time.time() - start_time))