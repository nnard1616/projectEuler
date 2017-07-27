stuff = []
for a in range(2, 101):
    for b in range(2, 101):
        n = a**b
        try:
            stuff.index(n)
        except:
            stuff.append(n)
            
print len(stuff)
