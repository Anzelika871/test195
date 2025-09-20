a = int(input())
b = 0
for i in range(0, a):
    if (i%3 == 0 or i%5 == 0):
        print(i)
        b += i
print(b)