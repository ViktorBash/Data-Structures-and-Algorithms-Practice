"""
Circular Linked Lists in Python

To find the end: the last node points to self.head
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):  # Insert at start
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)

            cur_node = self.head

            while cur_node.next != self.head:
                cur_node = cur_node.next

            cur_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            if cur_node == self.head:
                break

    def remove(self, key):
        # If we want to remove the head
        if self.head.next == self.head and self.head.data == key:
            self.head = None
        elif self.head.data == key:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev_node = None
            while cur_node.next != self.head:
                prev = cur_node
                cur_node = cur_node.next
                if cur_node.data == key:
                    prev.next = cur_node.next
                    cur_node = cur_node.next

    def split_list(self):
if __name__ == "__main__":
    cllist = CircularLinkedList()
    # cllist.append("C")
    # cllist.append("D")
    # cllist.prepend("B")
    # cllist.prepend("A")
    # cllist.remove("C")
    cllist.print_list()
