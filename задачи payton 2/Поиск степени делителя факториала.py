def m(n, k):
    x = 0
    p = k
    while p <= n:
        x += n // p
        p *= k
    return x
n = int(input())
k = int(input())
if k < 2:
    print(k)
else:
    result = m(n, k)
    print(f"{result}")