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
    k = 1 #initial condition of k
    sk = s*k #initial condition of sk
    if p > 1000:
        return
    else:
        while p <= 1000:#goes through scaled versions of s that have p less than 1000
            solutions.append(sk)
            perimeters.append(p)            
            k+=1
            sk = s*k
            p = numpy.dot(sk.A1, u.A1)

    s1 = T1*s
    s2 = T2*s
    s3 = T3*s
    generate_triples(s1)
    generate_triples(s2)
    generate_triples(s3)
    
generate_triples(solution)

smax = 0
for p in perimeters:
    if perimeters.count(p) > smax:
        smax = perimeters.count(p)
        print p, smax
