# let's enter two integers
print("enter two integers")
a, b = map(int, input().split())
m, n = a, b
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m
print("НОД=", m)
print("НОК=", a * b // m)