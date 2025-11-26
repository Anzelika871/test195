class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete(self, data):
        if self.is_empty():
            print("-")
            return
        # Если удаляемый элемент - первый
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print("-")
    def display(self):
        if self.is_empty():
            print("-")
            return
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
def main():
    my_linked_list = LinkedList()
    while True:
        choice = input("Выберите действие: ")
        if choice == '1':
            if my_linked_list.is_empty():
                print("False")
            else:
                print("True")
        elif choice == '2':
            data = input("Данные для добавления в конец: ")
            my_linked_list.append(data)
            print(f"Элемент '{data}' добавлен в конец списка")
        elif choice == '3':
            data = input("Добавления в начало: ")
            my_linked_list.prepend(data)
            print(f"Элемент '{data}' добавлен в начало списка")
        elif choice == '4':
            data = input("Данные для удаления: ")
            my_linked_list.delete(data)
        elif choice == '5':
            print("Список:")
            my_linked_list.display()
if __name__ == "__main__":
    main()