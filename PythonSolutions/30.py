answer = 0
for i in range(1, 1000000):
    s = 0
    for c in str(i):
        s += int(c)**5
        
    if i == s:
        print i
        answer+= i
        
print "\n", answer
