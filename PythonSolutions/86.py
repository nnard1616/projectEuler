# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:08:08 2016

@author: Nathan
"""

#fails the under 1 min rule, definitely some optimizations can be made, but too lazy
import time
import numpy
start_time = time.time()


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
v = numpy.matrix([1,1,0]) 

solutions = []
cuboidSize = 1815
def generate_triples(s):
#    p = numpy.dot(s.A1, u.A1)
    l = numpy.dot(s.A1, v.A1)
    k = 1 #initial condition of k
    sk = s*k #initial condition of sk
    if l > cuboidSize*3:
        return
    else:
        while l <= cuboidSize*3:
            triple = tuple(sk.transpose().tolist()[0])
            solutions.append(triple)          
            k+=1
            sk = s*k
#            p = numpy.dot(sk.A1, u.A1)
            l = numpy.dot(sk.A1, v.A1)

    s1 = T1*s
    s2 = T2*s
    s3 = T3*s
    generate_triples(s1)
    generate_triples(s2)
    generate_triples(s3)
    
generate_triples(solution)

cuboids = set()

while len(cuboids) <1000000:
    cuboids = set()

    
    for solution in solutions:
        dim = solution[0:2]
        for d in dim:
            for i in range(1,d/2+1):
                l = i
                w = d-i
                h = dim[dim.index(d)-1]
                if l > cuboidSize or w > cuboidSize or h > cuboidSize:
                    continue
                cuboid = [l,w,h]
                cuboid.sort()
                l,w,h = cuboid
                s1 = (l**2+(w+h)**2)**0.5
                s2 = (w**2+(l+h)**2)**0.5
                s3 = (h**2+(w+l)**2)**0.5
                
                mins = min(s1,s2,s3)
                if mins == int(mins):
                    cuboids.add((l,w,h))

                
            
    print cuboidSize, len(cuboids)
    cuboidSize +=1
print "done"



print("--- %s seconds ---" % (time.time() - start_time))
