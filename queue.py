class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None

    def dequeue(self):
        if self.first is None:
            return None

        node = self.first
        self.first = node.next
        if node is self.last:
            self.last = None
        return node

    def enqueue(self, node):
        if self.first is None:
            self.first = node
            self.last = node

        self.last.next = node
        self.last = node

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(Node(12))
    queue.enqueue(Node(1))
    queue.enqueue(Node(13))

    node = queue.dequeue()
    while node:
        print(node.data)
        node = queue.dequeue()
