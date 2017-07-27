from random import randint
def gcd(a, b):
    if (a%b == 0):
        return b
    else:
        return gcd(b, a%b)
        
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
#    
def factors(n, f=[]):
    if (n%2 == 0): #Step 0: eliminate factors of 2
        f.append(2)
        return factors(n/2, f)
    a =1
    while a == 1:
        a = randint(2, n-1) #Step 1: pick a random integer a, a < n
    if (gcd(a, n) != 1): #Step 2/3: Calculate gcd(a,n) and check if it != 1.  

        if is_prime(gcd(a, n)):
            f.append(gcd(a, n))
        else:
            f.extend(factors(gcd(a, n)))
            

        n = n/gcd(a, n)

        
        if is_prime(n):
            f.append(n)
        else:
            f.extend(factors(n))
        return f
    r = 1
    while True: #Step 4
        if (a**(1+r)%n) == (a%n):
            break
        else:
            r+=1
    if r%2 == 1: #Step5
        return factors(n, f)
    if (a**(r/2)%n) == -1%n: #Step6
        return factors(n, f)

    if is_prime(gcd(a**(r/2)+1,n)):
        f.append(gcd(a**(r/2)+1,n))
    else:
        f.extend(factors(gcd(a**(r/2)+1,n)))

    if is_prime(gcd(a**(r/2)-1,n)):
        f.append(gcd(a**(r/2)-1,n))
    else:
        f.extend(factors(gcd(a**(r/2)-1,n)))
    return f

def clean_up(n, f):
    truncated = []
    for factor in f:
        if n%factor == 0:
            truncated.append(int(factor))
            n = n/factor
    truncated.sort()
    return truncated
            

print clean_up(100 , factors(100 ))

#for n in range(775145, 1, -2):
#    if is_prime(n):
#        if (600851475143%n == 0):
#            print n
#            break


