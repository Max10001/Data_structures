from linked_list import Node

class Stack:

    def __init__(self):
        self.head = None

    def push(self, node):
        if self.head in None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return None

        node = self.head
        self.head = node.next
        return node

    def vizualization(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    if __name__ == "__main__":
        stack = Stack()
        stack.push(Node(15))
        stack.push(Node(20))
        stack.push(Node(55))
        stack.push(Node(13))

        print('recent element:', stack.pop().data)
        stack.vizualization()
