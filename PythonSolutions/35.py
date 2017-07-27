
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
def reorder(n):
    n = n[1:]+n[0]
    return n

count = 0
f = open("primes1000000.txt", "r")
primes = f.readline()
primes = primes.split(", ")
f.close()
primes[-1] = primes[-1][:-1]


for p in primes:
    
    for i in range(len(p)):
        circular = True
        p = reorder(p)
        if primes.count(p) == 1:
            pass
        else:
            circular = False
            break
    if circular == True:
        count +=1
        
print count
