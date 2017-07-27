# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 22:38:01 2016

@author: Nathan
"""

import time

start_time = time.time()


romeToNum = {}
romeToNum["\n"] = 0
romeToNum["I"] = 1
romeToNum["V"] = 5
romeToNum["X"] = 10
romeToNum["L"] = 50
romeToNum["C"] = 100
romeToNum["D"] = 500
romeToNum["M"] = 1000

numToRome = {}
numToRome[1] = "I"
numToRome[4] = "IV"
numToRome[5] = "V"
numToRome[9] = "IX"
numToRome[10] = "X"
numToRome[40] = "XL"
numToRome[50] = "L"
numToRome[90] = "XC"
numToRome[100] = "C"
numToRome[400] = "CD"
numToRome[500] = "D"
numToRome[900] = "CM"
numToRome[1000] = "M"



def roman_to_numeral(roman): 
    numeral = 0
    for i in range(len(roman)):
        try:
            if romeToNum[roman[i]] >= romeToNum[roman[i+1]]:
                numeral += romeToNum[roman[i]]
            else:
                numeral -= romeToNum[roman[i]]
        except:
            numeral += romeToNum[roman[i]]
    return numeral

def numeral_to_roman(numeral):
    roman = ""
    while numeral != 0:
        if int(numeral/1000) >= 1:
            roman += numToRome[1000]
            numeral -= 1000
            continue
        if int(numeral/900) >= 1:
            roman += numToRome[900]
            numeral -= 900
            continue
        if int(numeral/500) >= 1 :
            roman += numToRome[500]
            numeral -= 500
            continue
        if int(numeral/400) >= 1:
            roman += numToRome[400]
            numeral -= 400
            continue
        if int(numeral/100) >= 1:
            roman += numToRome[100]
            numeral -= 100
            continue
        if int(numeral/90) >= 1:
            roman += numToRome[90]
            numeral -= 90
            continue
        if int(numeral/50) >= 1:
            roman += numToRome[50]
            numeral -= 50
            continue
        if int(numeral/40) >= 1:
            roman += numToRome[40]
            numeral -= 40
            continue
        if int(numeral/10) >= 1:
            roman += numToRome[10]
            numeral -= 10
            continue
        if int(numeral/9) >= 1:
            roman += numToRome[9]
            numeral -= 9
            continue
        if int(numeral/5) >= 1:
            roman += numToRome[5]
            numeral -= 5
            continue
        if int(numeral/4) >= 1:
            roman += numToRome[4]
            numeral -= 4
            continue
        if int(numeral/1) >= 1:
            roman += numToRome[1]
            numeral -= 1
            continue
    return roman
saved = 0
f= open("p089_roman.txt", "r")
for line in f.readlines():
    line = line.split()[0]
    numeral = roman_to_numeral(line)
    betterRoman = numeral_to_roman(numeral)
    saved += (len(line) - len(betterRoman))
print saved

f.close()            

    
print("--- %s seconds ---" % (time.time() - start_time))