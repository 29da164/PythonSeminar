import numpy as np
import matplotlib.pyplot as plt

x1, x2 = input().split(" ")
x1 = int(x1)
x2 = int(x2)
d, n = input().split(" ")
d = int(d)
n = int(n)
a = []
for i in range(d+1):
    a.append(float(input()))

x = np.linspace(x1,x2,401)
y = np.zeros(401)
for j in range(401):
    for i in range(d+1):
        y[j] += a[i]*(x[j]**(i))

xx = np.linspace(x1,x2,n+1)
yy = np.zeros(n+1)
for j in range(n+1):
    for i in range(d+1):
        yy[j] += a[i]*(xx[j]**(i))


plt.plot(x,y)
plt.plot(xx,yy)
plt.scatter(xx,yy,marker="o",c="red")
plt.show()
