from math import factorial
def factSum(n):
    s = 0
    for d in str(n):
        s += factorial(int(d))
    return s
    
s = 0
for n in range(3, 1000001):
    if n == factSum(n):
        s+= n
        print n
print "Sum is ", s
