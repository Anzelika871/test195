def binary_search(a, b):
    left = 0
    right = len(a) - 1
    while left <= right:
        m = (left + right) // 2
        if a[m] == b:
            return m
        elif a[m] < b:
            left = m + 1
        else:
            right = m - 1
    return -1
print("Введите отсортированные числа через пробел:")
numbers = list(map(int, input().split()))
print("Введите число для поиска:")
number = int(input())
result = binary_search(numbers, number)
if result != -1:
    print(f"Индекс: {result}")
else:
    print(result)