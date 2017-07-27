
import time
start_time = time.time()
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n ** 0.5) # square root of n
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

def get_primes(n):
    primes = []
    while n%2 == 0:
        primes.append(2)
        n /= 2
    for x in range(1,n+1,2):
        if is_prime(x):
            while n%x == 0:
                primes.append(x)
                n /= x
    return primes

dmax = 0
n = 0

while dmax <= 500:
    n+=1
    tri = (n*(n+1))/2
    div = 0
    for x in range(1, int((tri)**0.5)+1):
        if tri%x == 0:
            div += 2

    dmax = max(dmax, div)
print n, (n*(n+1))/2, dmax
print time.time() - start_time, "seconds"

#dmax = 0
#n = 0
#while dmax < 10:
#    n+=1
#    div = 1
#    primes = get_primes((n*(n+1))/2)
#    for p in list(set(primes)):
#        div *= primes.count(p)+1
#    dmax = max(dmax, div)
#    print n, (n*(n+1))/2, primes, dmax    
#print time.time() - start_time, "seconds"
