coins = [1, 2, 5, 10, 20, 50, 100, 200] 

t= 200
combos = 0

for a in range(200, -1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                            combos+=1


print combos
