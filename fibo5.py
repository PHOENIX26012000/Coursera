m, n = [int(i) for i in input().split()]

if n<=1:
    print(n)
    quit()


l_n = (n+2)%60
l_m = (m+1)%60


def fibo(n):
    a,b = 0, 1
    for i in range(2,n+1):
        c = a+b
        c = c%10
        b, a = c, b
    return (c-1)
if l_n<=1:
    a = l_n-1
else:
    a = fibo(l_n)
if l_m<=1:
    b = l_m-1
else:
    b = fibo(l_m)

if a>=b:
    print(a-b)
else:
    print(10+a-b)
