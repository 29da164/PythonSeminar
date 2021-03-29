
import numpy as np
import matplotlib.pyplot as plt

N=400

z = [0 for i in range(N+1)]
a = [1 for i in range(10)]
b = [1 for i in range(10)]

n = int(input())
x = []
y = []
for i in range(n):
    xx, yy = map(float, input().split(" "))
    x.append(xx)
    y.append(yy)
xstep = (x[n-1]-x[0])/N

for i in range(10):
    a[i]=1.0
    b[i]=1.0
for i in range(N+1):
    z[i] = 0.0
for i in range (n):
    for j in range(n):
        if i!=j:
            b[i] *= (x[i]-x[j])

xx = x[0]
for k in range(N+1):
    for i in range(n):
        a[i] = 1.0
        for j in range(n):
            if i!=j:
                a[i] *= (xx-x[j])
        z[k] += y[i]*a[i]/b[i]
    print(xx,z[k])
    xx += xstep

xp = np.linspace(x[0],x[n-1],N+1)
plt.scatter(x,y,marker="o",c="red",s=100)
plt.plot(xp,z)
plt.show()
