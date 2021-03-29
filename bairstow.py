import random
import math

def quadratic(p, q):
    # Quadratic equation solver
    if p*p-4*q>0:
        print(-p/2 + math.sqrt(p*p-4*q)/2)
        print(-p/2 - math.sqrt(p*p-4*q)/2)
    else:
        print(-p/2, "+", math.sqrt(-p*p+4*q)/2, "i")
        print(-p/2, "-", math.sqrt(-p*p+4*q)/2, "i")

def bs(n, a, p, q):
    # Bairstow method
    EPS = 0.00001
    p = random.random() # initialize p as a random value
    q = random.random() # initialize q as a random value
    while 1:
        b[0] = 1 # !!warning !! potential bug
        b[1] = a[1]-p*a[0]
        for i in range(2,n+1):
            b[i] =  a[i]   -p*b[i-1] -q*b[i-2]
        c[1] = -1
        c[2] = -b[1]-p*c[1]
        for i in range(3,n+1):
            c[i] = -b[i-1] -p*c[i-1] -q*c[i-2]
        d[1] = 0
        d[2] = -1
        for i in range(3,n+1):
            d[i] = -b[i-2] -p*d[i-1] -q*d[i-2]
        dp = (-b[n-1]*d[n]+b[n]*d[n-1])         /(c[n-1]*d[n]-d[n-1]*(c[n]+b[n-1]))
        dq = (-b[n]*c[n-1]+b[n-1]*(c[n]+b[n-1]))/(c[n-1]*d[n]-d[n-1]*(c[n]+b[n-1]))
        if math.fabs(dp)>EPS or math.fabs(dq)>EPS:
            p += dp
            q += dq
        else:
            break
    for i in range(0,n):
        a[i]=b[i]
    return n, a, p, q


a = [0,0,0,0,0,0,0,0,0,0]
b = [0,0,0,0,0,0,0,0,0,0]
c = [0,0,0,0,0,0,0,0,0,0]
d = [0,0,0,0,0,0,0,0,0,0]
p = 0
q = 0
n = int(input())
for i in range(n):
    a[i] = int(input())
n = n-1
while 1:
    if n==0:
        break
    if n==1:
        print(-a[1]/a[0])
        break
    if n==2:
        quadratic(a[1], a[2]) # !!warning !! potential bug
        break
    if n>2:
        n, a, p, q = bs(n, a, p, q)
        quadratic(p, q) # !!warning !! potential bug
        n += -2