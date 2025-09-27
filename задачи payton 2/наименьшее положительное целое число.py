def m(a, b):
    return sorted(str(a)) == sorted(str(b))
def c(k1):
    k2 = k1 + 1
    n = 1
    while True:
        p1 = n * k1
        p2 = n * k2
        if m(p1, p2):
            return n
        n += 1
k1 = int(input())
result = c(k1)
print(f"{k1+1}, {result}")

