a, b = [int(i) for i in input().split()]

def lcm(a, b):
    if b == 0:
        return a
    c = a%b
    return lcm(b, c)

if a>b:
    l1 = lcm(a, b)
else:
    l1 = lcm(b, a)

print(a*b//l1)
