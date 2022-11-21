class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def vizualization(self, level):
        print(" " * level * 2 + str(self.data))
        if self.right is not None:
            self.right.vizualization(level + 1)

        if self.left is not None:
            self.left.vizualization(level + 1)

class BinaryTree:
    def __init__(self):
        self.root = None

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(12)

    n1 = Node(16)
    n1.left = Node(18)
    n1.left.right = Node(25)
    n1.right = Node(15)

    tree.root.left = n1

    n2 = Node(55)
    n2.left = Node(67)
    n2.right = Node(87)
    tree.root.right = n2
    tree.root.vizualization(0)

