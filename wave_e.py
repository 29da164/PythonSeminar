import math
N = 300
ex_old = []
ex_now = []
ex_new = []

T = int(input())
for i in range(N):
    ex_old.append(0)
    ex_now.append(0)
    ex_new.append(0)

for t in range(1,T+1,1):
    ex_now[int(N/2)] = math.exp(-0.5*(40-t)*(40-t)/144)
    for i in range(2,N-1,1):
        ex_new[i] = 2*ex_now[i] - ex_old[i] \
        + (ex_now[i-1] - 2*ex_now[i] + ex_now[i+1])/4
    for i in range(1,N,1):
        ex_old[i] = ex_now[i]
        ex_now[i] = ex_new[i]

for i in range(N):
    print(i, end=" ")
    print(ex_now[i])
