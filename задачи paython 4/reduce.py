class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def reduce(head, func, initial_value):
    current = head
    result = initial_value
    while current:
        result = func(result, current.data)
        current = current.next
    return result
def add(acc, curr):
    return acc + curr
def multiply(acc, curr):
    return acc * curr
print("Числа для списка:")
values = list(map(int, input().split()))
if values:
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
else:
    head = None
print("\n Операцию:")
x = int(input())
if x == 1:
    result = reduce(head, add, 0)
    print(f"\n Сумма: {result}")
elif x == 2:
    result = reduce(head, multiply, 1)
    print(f"\n Произведение: {result}")
else:
    print("-")
