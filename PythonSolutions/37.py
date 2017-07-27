



f= open("primes1000000.txt", "r")
primes = f.read().split(", ")
primes[-1] = primes[-1][:-1]

f.close()

s = 0


def is_all_prime(n): #checks if all truncations of n are prime.  feed int, return boolean.
    allPrime = True
    sn = str(n)
    for i in range(len(sn)):
        if primes.count(str(sn[i:])) == 0:
            allPrime = False
            break
        if primes.count(str(sn[:i+1])) == 0:
            allPrime = False
            break
    return allPrime
    
for p in primes[4:]:
    if is_all_prime(int(p)):
        s+=int(p)
print s
    
    


