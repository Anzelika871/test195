class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left = TreeNode(data)
                    break
                current = current.left
            elif data > current.data:
                if not current.right:
                    current.right = TreeNode(data)
                    break
                current = current.right
            else:
                break
    def search(self, data):
            current = self.root
            while current:
                if data == current.data:
                    return current
                elif data < current.data:
                    current = current.left
                else:
                    current = current.right
            return None
    def in_order_traversal(self):
            result = []
            stack = []
            current = self.root
            while stack or current:
                while current:
                    stack.append(current)
                    current = current.left
                current = stack.pop()
                result.append(current.data)
                current = current.right
            return result
    def pre_order_traversal(self):
            if not self.root:
                return []
            result = []
            stack = [self.root]
            while stack:
                current = stack.pop()
                result.append(current.data)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
            return result
    def post_order_traversal(self):
            if not self.root:
                return []
            result = []
            stack1 = [self.root]
            stack2 = []
            while stack1:
                current = stack1.pop()
                stack2.append(current)
                if current.left:
                    stack1.append(current.left)
                if current.right:
                    stack1.append(current.right)
            while stack2:
                result.append(stack2.pop().data)
            return result
tree = BinaryTree()
print("Количество узлов для добавления ")
n = int(input())
for i in range(n):
    value = int(input(f"\n Узел {i+1}: "))
    tree.insert(value)
print("\n Поиск:")
search_val = int(input("\n Что ищем? "))
found = tree.search(search_val)
print(f"\n Найдено: {found}")
print(f"\n In-order: {tree.in_order_traversal()}")
print(f"\n Pre-order: {tree.pre_order_traversal()}")
print(f"\n Post-order: {tree.post_order_traversal()}")
