n, m = input().split(" ")
n = int(n)
m = int(m)
print(m)
x = []
y = []
for i in range(n):
    xx, yy = map(float, input().split(" "))
    x.append(xx)
    y.append(yy)

a = [[0 for i in range(n+1)] for j in range(n)]

for i in range(m):
    for j in range(m):
        for k in range(n):
            a[i][j]+= x[k]**(i+j)
        print(a[i][j])
    for k in range(n):
        a[i][n] += y[k]*x[k]**i
    print(a[i][n]) 