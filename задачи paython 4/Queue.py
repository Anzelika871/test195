class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item, priority = 5):
        self.items.append((item, priority))
        self.sort_queue()
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)[0]
    def front(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0][0]
    def size(self):
        return len(self.items)
    def sort_queue(self):
        self.items.sort(key=lambda x: x[1])
my_queue = Queue()
print("Элементы для добавления в очередь: ")
n = int(input())
for i in range(n):
    print(f"Элемент {i + 1}")
    item = input("Элемент: ")
    priority = int(input("Приоритет: "))
    my_queue.enqueue(item, priority)
    print("\n Очередь: ", my_queue.items)
if not my_queue.is_empty():
    print(f"\n Первый элемент: {my_queue.front()}")
    print(f"\n Размер очереди: {my_queue.size()} ")
    print("\n Количество элементов для удаления: ")
    m = int(input())
    for i in range(min(m, my_queue.size())):
        try:
            y = my_queue.dequeue()
            print(f"\n Удаленно: {y}")
        except IndexError as e:
            print(e)
            break
    print(f"\n После удаления: {my_queue.items}")
    print(f"\n Размер очереди: {my_queue.size()}")
    print(f"\n Очередь пустая? {my_queue.is_empty()}")
else:
    print("Очередь пуста")

