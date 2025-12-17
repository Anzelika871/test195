class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def map_linked_list(head, mapping_function):
    if not head:
        return None
    new_head = Node(mapping_function(head.data))
    current_old = head.next
    current_new = new_head
    while current_old:
        current_new.next = Node(mapping_function(current_old.data))
        current_new = current_new.next
        current_old = current_old.next
    return new_head
print("Числа для списка:")
values = list(map(int, input().split()))
if values:
    original_list = Node(values[0])
    current = original_list
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
else:
    original_list = None
print("\n Преобразование:")
a = int(input())
if a == 1:
    def mapping_function(x):
        return x * 2
elif a == 2:
    def mapping_function(x):
        return x + 10
elif a == 3:
    def mapping_function(x):
        return x ** 2
else:
    print("-")
    mapping_function = lambda x: x
if original_list:
    mapped_list = map_linked_list(original_list, mapping_function)
    print("\n Результат:")
    current = mapped_list
    while current:
        print(current.data, end= " - ")
        current = current.next
else:
    print("Список пуст")