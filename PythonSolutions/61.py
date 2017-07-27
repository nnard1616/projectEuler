# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 20:14:04 2016

@author: Nathan
"""

import time
import itertools
start_time = time.time()


def tri(n):
    return n*(n+1)/2
    
def quad(n):
    return n**2

def pent(n):
    return n*(3*n-1)/2
    
def hexa(n):
    return n*(2*n-1)
    
def hept(n):
    return n*(5*n-3)/2
    
def octa(n):
    return n*(3*n-2)

def main():
    n = 1
    tris = []
    quads = []
    pents = []
    hexas = []
    hepts = []
    octas = []
    figurates = {}
    
    while tri(n) <10000:
        if tri(n) >1009:
            tris.append(str(tri(n)))
        if quad(n) > 1009 and quad(n) < 10000:
            quads.append(str(quad(n)))
        if pent(n) > 1009 and pent(n) < 10000:
            pents.append(str(pent(n)))
        if hexa(n) > 1009 and hexa(n) < 10000:
            hexas.append(str(hexa(n)))
        if hept(n) > 1009 and hept(n) < 10000:
            hepts.append(str(hept(n)))
        if octa(n) > 1009 and octa(n) < 10000:
            octas.append(str(octa(n)))
        n+=1
        
    figurates['t'] = tris
    figurates['q'] = quads
    figurates['p'] = pents
    figurates['x'] = hexas
    figurates['h'] = hepts
    figurates['o'] = octas
    
    seqs = list(itertools.permutations(['q','p','x','h','o'],5))
    
    
    for t in figurates['t']:
        for seq in seqs:
            f1,f2,f3,f4,f5=seq
            for n1 in figurates[f1]:
                if t[2:] == n1[:2]:
                    for n2 in figurates[f2]:
                        if n1[2:] == n2[:2]:
                            for n3 in figurates[f3]:
                                if n2[2:] == n3[:2]:
                                    for n4 in figurates[f4]:
                                        if n3[2:] == n4[:2]:
                                            for n5 in figurates[f5]:
                                                if n4[2:] == n5[:2] and n5[2:] == t[:2]:
                                                    answer = [  t, n1, n2, n3, n4, n5]
                                                    print answer, sum(map(int, answer))
                                                    return figurates


    return figurates
    

figurates = main()

print("--- %s seconds ---" % (time.time() - start_time))