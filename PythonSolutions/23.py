import time
start_time = time.time()
def d (n):
    divisors = [1]
    for f in range(2, n):
        if divisors.count(f) > 0:
            return sum(divisors)
        if n%f ==0:
            divisors.append(f)
            if n/f != f:
                divisors.append(n/f)
    return sum(divisors)

def is_abun (n):
    if d(n) > n:
        return True
    else:
        return False

abundants = []
for n in range(12,  28124):
    if is_abun(n):
        abundants.append(n)

print abundants[:50]

noAbuns = range(1, 28124)
for n in abundants:
    if (abundants.index(n)%100 == 0):
        print abundants.index(n), "of", len(abundants), "processed."
    for m in abundants[abundants.index(n):]:
        if (n+m) > 28123:
            break  
        try:
            noAbuns.pop(noAbuns.index(n+m))
        except:
            pass
            
#is_sum = False
#for n in range(25, 28124):
#    if n%2 == 0 :
#        x = y = n/2
#    else:
#        x = n/2
#        y = x+1
#    while x >= 12:
#        if (abundants.count(x) == 1) and (abundants.count(y) == 1):
#            is_sum = True
#            break
#        x-=1
#        y+=1
#    if not(is_sum):
#        noAbuns.append(n)
#    is_sum = False
        
print time.time() - start_time, "seconds"
print sum(noAbuns), len(noAbuns)
print noAbuns[:50]
print noAbuns[-50:]
            
        
