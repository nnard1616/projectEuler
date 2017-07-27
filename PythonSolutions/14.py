import time
start_time = time.time()
cmax = 0
magicNum = 0
for x in range(10, 1000000):
    n = x
    c = 1
    while n != 1:
        if n%2 == 0:
            n /= 2
            c+=1
        else:
            n = 3*n+1
            c+=1
    if c > cmax:
        magicNum = x
        cmax = max(cmax, c)
print time.time() - start_time, "seconds"
print cmax, magicNum
