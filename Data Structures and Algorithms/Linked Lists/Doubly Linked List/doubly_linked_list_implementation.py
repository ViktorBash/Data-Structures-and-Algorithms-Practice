"""
Doubly Linked List Implementation in Python
(has a previous pointer unlike a singly linked list).
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur_head = self.head
            new_node = Node(data)
            new_node.next = cur_head
            cur_head.prev = new_node
            self.head = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def add_node_after(self, data, key):
        if self.head is None:
            return
        cur_node = self.head
        while cur_node.data != key:
            cur_node = cur_node.next
        new_node = Node(data)
        temp_next = cur_node.next
        cur_node.next = new_node
        new_node.next = temp_next
        if temp_next:
            temp_next.prev = new_node

    def add_node_before(self, data, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.prepend(data)
            return
        cur_node = self.head
        while cur_node.next.data != key:
            cur_node = cur_node.next
        temp_node = cur_node.next
        new_node = Node(data)
        cur_node.next = new_node
        new_node.prev = cur_node
        new_node.next = temp_node
        temp_node.prev = new_node
        return

    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head.next.prev = None
            self.head = self.head.next
            return

        cur_node = self.head
        while cur_node.next.data != data:
            cur_node = cur_node.next

        if cur_node.next.next:
            cur_node.next.next.prev = cur_node
        cur_node.next = cur_node.next.next


if __name__ == "__main__":
    dllist = DoublyLinkedList()
    # dllist.prepend(0)
    # dllist.append(1)
    # dllist.append(2)
    # dllist.append(3)
    # dllist.append(4)
    # dllist.prepend(-1)
    dllist.append("A")
    dllist.append("B")
    dllist.append("C")
    dllist.append("D")
    # dllist.add_node_after("E", "D")
    # dllist.add_node_before("E", "D")
    dllist.delete_node("B")
    dllist.print_list()

