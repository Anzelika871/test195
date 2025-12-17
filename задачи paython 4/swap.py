class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
def linked_list(*values):
        if not values:
            return LinkedList()
        lin = LinkedList()
        lin.head = Node(values[0])
        current = lin.head
        for value in values[1:]:
            current.next = Node(value)
            current = current.next
        return lin
def print_linked_list(linked_list):
        current = linked_list.head
        while current:
            print(current.value, end=" ")
            current = current.next
            if current:
                print("-", end=" ")
        print()
def get_node_and_prev(linked_list, index):
        if index < 0:
            return None, None
        current = linked_list.head
        prev = None
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1
        if count == index:
            return current, prev
        return None, None
def swap_nodes(list_pointer1, index1, list_pointer2, index2):
        if not list_pointer1 or not list_pointer2:
            return False
        list1 = list_pointer1[0]
        list2 = list_pointer2[0]
        if not list1 or not list2:
            return False
        node1, prev1 = get_node_and_prev(list1, index1)
        node2, prev2 = get_node_and_prev(list2, index2)
        if not node1 or not node2:
            return False
        if prev1:
            prev1.next = node2
        else:
            list1.head = node2
        if prev2:
            prev2.next = node1
        else:
            list2.head = node1
        x = node1.next
        node1.next = node2.next
        node2.next = x
        return True
print("Первый список: ")
values1 = list(map(int, input().split()))
list1 = linked_list(*values1)
print("\n Второй список: ")
values2 = list(map(int, input().split()))
list2 = linked_list(*values2)
print("\n Первый список:")
print_linked_list(list1)
print("\n Второй список:")
print_linked_list(list2)
index1 = int(input("Индекс 1: "))
index2 = int(input("Индекс 2: "))
result = swap_nodes([list1], index1, [list2], index2)
print(f"\n Результат: {result}")
print("\nПервый список после обмена:")
print_linked_list(list1)
print("Второй список после обмена:")
print_linked_list(list2)