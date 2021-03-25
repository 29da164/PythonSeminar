# Euler method: example d^2y/dx^2 = -y
# initial condition 1: y = 1, dydx = 0 ==> cosine
# initial condition 2: y = 0, dydx = 1 ==> sine

import matplotlib.pyplot as plt
x = 0
y = 1
dx = 0.001
dydx = 1
p = []
xx = []
for i in range(300):
    dydx += -y*dx
    y += dydx
    x += dx
    #print(x, y)
    p.append(y)
    xx.append(x)
plt.plot(xx,p)
plt.show()