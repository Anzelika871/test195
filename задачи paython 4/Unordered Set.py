class UnorderedSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    def _hash(self, value):
        return hash(value) % self.size
    def add(self, value):
        index = self._hash(value)
        if value not in self.buckets[index]:
            self.buckets[index].append(value)
    def remove(self, value):
        index = self._hash(value)
        if value in self.buckets[index]:
            self.buckets[index].remove(value)
    def contains(self, value):
        index = self._hash(value)
        return value in self.buckets[index]
    def elements(self):
        result = []
        for bucket in self.buckets:
            result.extend(bucket)
        return result
my_set = UnorderedSet()
print("Количество элементов для добавления")
n = int(input())
for i in range(n):
    value = input(f"Элемент {i + 1}: ")
    my_set.add(value)
print(f"\n Элементы в множестве: {my_set.elements()}")
print ("\n Элемент для проверки")
x = input()
print(f"\n Содержит ли множество? {my_set.contains(x)}")
print("\n Элемент для удаления:  ")
y = input()
my_set.remove(y)
print("Элементы после удаления:", my_set.elements())