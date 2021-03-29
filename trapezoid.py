def trape(d, n, x1, x2, a):
     s = 0
     x = x1
     h = (x2-x1)/n

     for i in range(n+1):
         x = x1+h*i
         if i==0 or i==n:
             for j in range(d+1):
                 s += a[j]*(x**j)*h/2
         else:
             for j in range(d+1):
                 s += a[j]*(x**j)*h
     return s

def exact(d, x1, x2, a):
     theory = 0
     for i in range(d+1):
         theory += a[i]/(i+1)*((x2**(i+1))-(x1**(i+1)))
     return theory

x1, x2 = input().split(" ")
x1 = int(x1)
x2 = int(x2)
d, n = input().split(" ")
d = int(d)
n = int(n)
a = []
for i in range(d+1):
     a.append(float(input()))

calc_result = trape(d, n, x1, x2, a)
theory_result = exact(d, x1, x2, a)

print("approx:\t",calc_result)
print("exact:\t",theory_result)
print("error:\t",theory_result - calc_result, end='  ')
print("(",(calc_result -  theory_result)/theory_result*100, "%)")
