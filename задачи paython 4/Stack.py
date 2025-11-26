class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return "Стек пуст!"
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return "Стек пуст!"
        return self.items[-1]
    def size(self):
        return len(self.items)
my_stack = Stack()
while True:
    command = input("\nВведите команду: ")
    if command == "1":
        item = input("Введите элемент для добавления: ")
        my_stack.push(item)
        print(f"Элемент '{item}' добавлен в стек")
    elif command == "2":
        popped_item = my_stack.pop()
        print(f"Удаленный элемент: {popped_item}")
    elif command == "3":
        top_item = my_stack.peek()
        print(f"Верхний элемент: {top_item}")
    elif command == "4":
        empty_status = my_stack.is_empty()
        print(f"Стек пуст: {empty_status}")
    elif command == "5":
        stack_size = my_stack.size()
        print(f"Размер стека: {stack_size}")
    elif command == "6":
        stack_items = my_stack.display()
        print(f"Содержимое стека: {stack_items}")
        break
    else:
        print("-")