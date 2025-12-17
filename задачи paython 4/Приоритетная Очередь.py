class PriorityQueue:
    def __init__(self):
        self.elements = []
    def is_empty(self):
        return len(self.elements) == 0
    def push(self, item, priority):
        self.elements.append((item, priority))
        self.elements.sort(key=lambda x: x[1])
    def pop(self):
        if self.is_empty():
            return None
        return self.elements.pop(0)[0]
    def peek(self):
        if self.is_empty():
            return None
        return self.elements[0][0]

    def size(self):
        return len(self.elements)
pq = PriorityQueue()
print("Количество элементов для добавления")
n = int(input())
for i in range(n):
    item = input(f"\n Элемент {i + 1}: ")
    priority = int(input(f"\n Приоритет: "))
    pq.push(item, priority)
print(f"\n Элемент с наивысшим приоритетом: {pq.peek()}")
print("\n Обработка всех элементов:")
while not pq.is_empty():
    print(pq.pop())