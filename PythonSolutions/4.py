import time
start_time = time.time()
lar = 0
for x in range(990, 900, -11):
    for y in range(999, 900, -1):
        if str(x*y) == str(x*y)[::-1]:
            lar = max(lar, x*y)
print time.time() - start_time, "seconds"
print lar


