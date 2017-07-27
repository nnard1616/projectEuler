n = 1
s = 1

for step in range(2, 1001, 2):
    for i in range(4):
        n+= step
        s += n
print s
