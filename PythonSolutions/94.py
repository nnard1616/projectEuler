# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 01:44:53 2016

@author: Nathan
"""
#finds all right triangles that have shortest side's double is within 1 of largest side and whose perimeter is less than 10^9
import time
start_time = time.time()
import numpy

T1 = numpy.matrix(([1, -2, 2],
                   [2, -1, 2],
                   [2, -2, 3]))

T2 = numpy.matrix(([1, 2, 2],
                   [2, 1, 2],
                   [2, 2, 3]))
                  
T3 = numpy.matrix(([-1, 2, 2],
                   [-2, 1, 2],
                   [-2, 2, 3]))

solution = numpy.matrix([3,4,5]).transpose() #pythagorean triple (or solution) column vector
u = numpy.matrix([1,1,1]) #for finding sum of three side lengths in a solution column vector
 
solutions = []
perimeters = []
def generate_triples(s):
    p = numpy.dot(s.A1, u.A1)
    ls = s.transpose().tolist()[0]
    
    if p > 1000000000 or abs(min(ls)*2-max(ls))!=1:
        return
    else:      
        solutions.append(s)

    s1 = T1*s
    s2 = T2*s
    s3 = T3*s

    generate_triples(s1)
    generate_triples(s2)
    generate_triples(s3)
    
generate_triples(solution)
s=0
for sol in solutions:
    lsol = sol.transpose().tolist()[0]
    s += (min(lsol)*2 + max(lsol)*2)#total perimeter of triangles formed by two of each right triangle (we don't count middle side at all, not part of perimeter)
print s
print("--- %s seconds ---" % (time.time() - start_time))