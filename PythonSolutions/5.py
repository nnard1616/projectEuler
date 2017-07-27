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

def factor_product(number):
    factors = []
    
    for n in range(2, number+1):
        if is_prime(n):
            factors.append(n)
        else:
            a = n
            for f in factors:
                if a%f == 0:
                    a = a/f
            if a !=1:
                factors.append(a)
    prod = 1
    for f in factors:
        prod *= f
    return prod


print factor_product(23)
print time.time() - start_time, "seconds"

