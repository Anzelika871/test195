class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
def count(head, value):
    count_val = 0
    current = head
    while current:
        if current.data == value:
            count_val += 1
        current = current.next
    return count_val
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
list_length = length(head)
print(f"\n Длина списка: {list_length}")
print("\n Число для подсчета ")
x = int(input())
y = count(head, x)
print(f"Число встречается {y} раз(а)")