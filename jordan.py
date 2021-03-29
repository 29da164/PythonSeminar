EPSILON = 0.001
n = int(input())
a = [[0 for x in range(n+1)] for y in range(n)]
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input())
for i in range(n):
    pivot = a[i][i]
    if abs(pivot) > EPSILON:
        for j in range(i, n+1):
            a[i][j] /= pivot
        for k in range(n):
            d = a[k][i]
            for j in range(i, n+1):
                if k!=i:
                    a[k][j] -= d*a[i][j]
    else:
        print("Pivot: ", pivot, "is too small.")
for i in range(n):
    print(a[i][n])