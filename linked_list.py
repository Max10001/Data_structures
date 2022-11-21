class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, node):
        if self.head is None:
            self.head = node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = node


    def vizualization(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.add(Node(3))
    linked_list.add(Node(5))
    linked_list.add(Node(6))

    linked_list.vizualization()
