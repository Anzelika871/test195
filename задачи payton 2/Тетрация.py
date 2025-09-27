import math
def tetration(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        return x ** tetration(x, n - 1)
def count_digits(n):
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1
x = float(input())
n = int(input())
if n < 0:
    print(n)
else:
    a = tetration(x, n)
    b = count_digits(a)
    print(f"{a}")
    print(f"{b}")