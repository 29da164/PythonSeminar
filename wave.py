import math
N = 300
ex = []
hy = []

T = int(input())
for i in range(N):
    ex.append(0)
    hy.append(0)

for t in range(T+1):
    for i in range(N):
        ex[i] = ex[i] + (hy[i-1] - hy[i])/2
    ex[int(N/2)] = math.exp(-0.5*(40-t)*(40-t)/144)
    for i in range(N-1):
        hy[i] = hy[i] + (ex[i] - ex[i+1])/2

for i in range(N):
    print(i, end=" ")
    print(ex[i])