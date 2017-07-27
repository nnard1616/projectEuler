def fibo(a,b,n):
    if (a>4000000):
        return n
    else:
        if (a%2==0):
            n += a
        return fibo(b, a+b, n)

print fibo(1,2,0)
