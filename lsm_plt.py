import jordan_lib
import numpy as np
import matplotlib.pyplot as plt
N = 400
n, m = input().split(" ")
n = int(n)
m = int(m)

x = []
y = []
for i in range(n):
    xx, yy = map(float, input().split(" "))
    x.append(xx)
    y.append(yy)

a = [[0 for i in range(m+1)] for j in range(m)]

for i in range(m):
    for j in range(m):
        for k in range(n):
            a[i][j]+= x[k]**(i+j)
    for k in range(n):
        a[i][m] += y[k]*x[k]**i

ans = jordan_lib.solve_jordan(m,a)

print("y=",end=" ")
for i in range(m):
    print("+",ans[i],"x^",i)

xp = np.linspace(x[0],x[n-1],N+1)

z = []
for j in range(N+1):
    zz = 0
    for i in range(m):
        zz += ans[i]*xp[j]**i
    z.append(zz)

plt.scatter(x,y, s=100, c="red")
plt.plot(xp,z)
plt.show()
