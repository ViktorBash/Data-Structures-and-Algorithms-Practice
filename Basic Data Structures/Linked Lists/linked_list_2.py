"""
Linked list in python
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:  # Nothing in the list, head pointer points to nothing
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # While the node wer are iterating through is not the tail
            last_node = last_node.next
        last_node.next = new_node  # Append node to the end of the list

    def print_list(self):
        cur_node = self.head
        while cur_node:  # While current node is not None
            print(cur_node.data)
            cur_node = cur_node.next  # Move to next node

    def prepend(self, data):
        new_node = Node(data)  # Create node

        new_node.next = self.head  # Point to the head
        self.head = new_node  # The head is the new node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        # In case the node to delete is the head node
        if cur_node and cur_node.data == key:  # If cur_Node is not none and the data is the data we put in
            self.head = cur_node.next
            cur_node = None
            return

        # Moving through the list to the node to delete, setting previous node so we know it for later
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # In case the element to delete is not in the list
        if cur_node is None:
            return

        prev.next = cur_node.next  # Fixing the pointer for the node before the deleted node
        cur_node = None  # Removes the element from the list

    def delete_node_position(self, position):
        cur_node = self.head

        # Checking if the node to delete is the head
        if position == 0:
            self.head = cur_node.next
            cur_node = None
            return

        # Iterating through until we reach the position or the end of the list
        prev = None
        i = 0
        while cur_node and i != position:
            prev = cur_node
            cur_node = cur_node.next
            i += 1

        # If the cur_node is None (we reached end of list without getting to the position)
        if cur_node is None:
            return

        # Here we have reached the position
        prev.next = cur_node.next  # Fixing the pointer
        cur_node = None  # Deleting the node

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    # The node argument should be the head to get the proper length
    def length_recursive(self, node):
        if node is None:  # Exit case
            return 0
        return 1 + self.length_recursive(node.next)

    def node_swap(self, key_1, key_2):
        # If both keys are the same, we can't swap the same thing
        if key_1 == key_2:
            return

        # Setup
        prev_1 = None
        cur_1 = self.head

        # Iterating through 1st node to swap to get it
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        # Setup
        prev_2 = None
        cur_2 = self.head

        # Getting the 2nd node through iterating until the key matches the node we are on
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        # In case one of the nodes does not actually exist, we will just return
        if not cur_1 or not cur_2:
            return

        # The else condition is in case the node is the head node
        if prev_1:  # Check if the 1st previous node exists, (to see if the node to swap is the head)
            prev_1.next = cur_2  # Changing pointer

        else:
            self.head = cur_2

        if prev_2:  # Same thing
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next















# llist = LinkedList()
# llist.append("B")
# llist.append("C")
# llist.prepend("A")
# llist.insert_after_node(llist.head.next, "E")
# llist.delete_node("B")
# llist.print_list()

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.print_list()

# print("Now deleting node")
# llist.delete_node_position(2)
# llist.print_list()
# print(llist.length())
# print(llist.length_recursive(llist.head))

print("Swap Nodes")
llist.node_swap("B", "C")
llist.print_list()

