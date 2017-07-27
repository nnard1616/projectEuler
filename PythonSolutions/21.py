import string
d = dict(zip(list(string.uppercase), range(1, 27)))

names = open("names.txt", 'r').readlines()[0].replace('"', '').split(",")
names.sort()

tot = 0
for name in names:
    tot += sum(map(lambda x: d[x], list(name)))*(names.index(name)+1)
print tot
