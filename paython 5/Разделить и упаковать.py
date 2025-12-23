def knapsack_recursive(items, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    weight, value = items[n - 1]
    if weight > capacity:
        return knapsack_recursive(items, capacity, n - 1)
    else:
        exclude = knapsack_recursive(items, capacity, n - 1)
        include = value + knapsack_recursive(items, capacity - weight, n - 1)
        return max(exclude, include)
def solve_knapsack(items, capacity):
    return knapsack_recursive(items, capacity, len(items))
test_cases = [
    {
        "items": [(2, 10), (3, 15), (5, 30)],
        "capacity": 5,
        "expected": 30
    },
    {
        "items": [(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)],
        "capacity": 10,
        "expected": 50
    },
    {
        "items": [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)],
        "capacity": 7,
        "expected": 55
    }
]

for i, test in enumerate(test_cases, 1):
    items = test["items"]
    capacity = test["capacity"]
    expected = test["expected"]

    result = solve_knapsack(items, capacity)

    print(f"Рюкзак {i}:")
    print(f"  Предметы: {items}")
    print(f"  Вместимость рюкзака: {capacity}")
    print(f"  Полученный результат: {result}")