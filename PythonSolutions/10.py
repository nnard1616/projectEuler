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

print sum(map(lambda x: x if is_prime(x) else False, range(1, 2000000, 2)))+2
print time.time() - start_time, "seconds"

#marked = [0] * 2000000
#value = 3
#s = 2
#while value < 2000000:
#    if marked[value] == 0:
#        s += value
#        i = value
#        while i < 2000000:
#            marked[i] = 1
#            i += value
#    value += 2
#print s
