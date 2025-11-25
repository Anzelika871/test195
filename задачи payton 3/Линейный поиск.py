def linear_search(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i
    return -1
print("Введите числа через пробел:")
numbers = list(map(int, input().split()))
print("Введите число для поиска:")
number = int(input())
result = linear_search(numbers, number)
if result != -1:
    print(f"Индекс: {result}")
else:
    print(result)