nums = range(10, 100)
for n in nums:
    if n%10 ==0:
        nums.pop(nums.index(n))
        
def gcd(a, b):
    if (a%b == 0):
        return b
    else:
        return gcd(b, a%b)

def check(num, den): #feed strings, return true or false
    onum = int(num)
    oden = int(den)
    
        
    for n in num:
        if den.count(n) >0:
            num = num.replace(n, "")
            den = den.replace(n, "")
            if num == "":
                num = n
            if den == "":
                den = n
    if float(num)/int(den) == float(onum)/oden and int(num)!=onum:
        return [int(num), int(den)]
    else:
        return [0,0]

prod = 1
for n in nums:
    for nr in nums[-1::-1]:
        if nr > n:
            d= check(str(n), str(nr))
            if d[1] >0:
                print d
                
                

            
