from itertools import permutations

items = [1,2,3,4,5,6,7,8,9,"*","*"]
perms = permutations(items)

def combine(n):
    s = ""
    for item in n:
        s += str(item)
    return s


pan = []
for p in perms:
    literal = combine(p)
    nums = literal.split("*")
    try:
        if (int(nums[0]) * int(nums[1]) == int(nums[2])) and pan.count(int(nums[2])) == 0:
            pan.append(int(nums[2]))
    except:
        pass
            
    
print pan
