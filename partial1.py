lamb = 80.4
rho = 7874
c = 461
dx = 0.1
N = 10
u_old = []
u_new = []
for i in range(0,N+1,1):
    u_old.append(1000)
    u_new.append(0)

u_old[0]=300
u_old[N]=300

for t in range(3600):
    for i in range(1,N,1):
        u_new[i] = u_old[i] + lamb/(rho*c*dx*dx)*(u_old[i+1] - 2*u_old[i] + u_old[i-1])
    for i in range(1,N,1):
        u_old[i] = u_new[i]
    if (t%10==0) and (t%60==0):
        print(t, end=" ")
        for i in range(N+1):
            print(u_old[i], end = " ")
        print()
