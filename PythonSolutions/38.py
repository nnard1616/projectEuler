

def has_all_nums(n): #checks if n is pandigital.  Feed string, return boolean.
    isPan = True
    for d in range(1,10):
        if n.count(str(d)) !=1:
            isPan = False
    return isPan
m = 0
for n in range(10000):
    pan=""
    i = 1
    while len(pan) < 9:
        pan+=str(n*i)
        i+=1
    if len(pan) == 9:
        if has_all_nums(pan):
            m = max(m, int(pan))
print m
