N = int(input())
a = [input().split(" ") for i in range(N)]
a = [[float(v) for v in l] for l in a]
x = [0 for i in range(N)]
for k in range(50):
    for i in range(N):
        x[i] = a[i][N]
        for j in range(N):
            if i!=j:
                x[i] -=a[i][j]*x[j]
        x[i] /= a[i][i]
    print(k)
    for i in range(N):
        print(x[i]) 
