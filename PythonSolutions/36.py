def convert_ten_to_x(t, x): #t is the base ten number to be converted to base x.  Feed int, return int.
    basex = ""
    digits = []
    p = 0
    while x**p < t:
        p+=1
    if x**p != t:
        p-=1
    for n in range(p+1):
        digits.append(0)
        
        
    while t>0:
        p = 0
        while x**p < t:
            p+=1
        if x**p != t:
            p-=1
        while t >= x**p:
            t-=x**p
            digits[p]+=1
        
    for d in digits[::-1]:
        basex += str(d)
    if basex == "":
        basex=0
    return int(basex)
    
def convert_x_to_ten(n, x): #n is a number in base x; convert n to base ten.  Feed int, return int.
    t = 0
    digits = []
    for d in str(n):
        digits.append(int(d))
    digits.reverse()
    
    for i in range(len(digits)):
        t+=(digits[i]*x**i)
        
    return t
    
def is_palindromic(n): #checks if n is a palindromic number.  Feed int, return boolean
    sn = str(n)
    if sn == sn[::-1]:
        return True
    else:
        return False

s = 0
for n in range(1000000):
    if is_palindromic(n) and is_palindromic(convert_ten_to_x(n, 2)):
        s+=n
print s
