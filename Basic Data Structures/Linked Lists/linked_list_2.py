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

    # def node_swap(self, key_1, key_2):
    #     # If both keys are the same, we can't swap the same thing
    #     if key_1 == key_2:
    #         return
    #
    #     # Setup
    #     prev_1 = None
    #     cur_1 = self.head
    #
    #     # Iterating through 1st node to swap to get it
    #     while cur_1 and cur_1.data != key_1:
    #         prev_1 = cur_1
    #         cur_1 = cur_1.next
    #
    #     # Setup
    #     prev_2 = None
    #     cur_2 = self.head
    #
    #     # Getting the 2nd node through iterating until the key matches the node we are on
    #     while cur_2 and cur_2.data != key_2:
    #         prev_2 = cur_2
    #         cur_2 = cur_2.next
    #
    #     # In case one of the nodes does not actually exist, we will just return
    #     if not cur_1 or not cur_2:
    #         return
    #
    #     # The else condition is in case the node is the head node
    #     if prev_1:  # Check if the 1st previous node exists, (to see if the node to swap is the head)
    #         prev_1.next = cur_2  # Changing pointer
    #
    #     else:
    #         self.head = cur_2
    #
    #     if prev_2:  # Same thing
    #         prev_2.next = cur_1
    #     else:
    #         self.head = cur_1
    #
    #     cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def node_swap(self, key1, key2):
        if key1 == key2:
            return

        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1
        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    # A --> B --> C --> D --> None
    # D --> C --> B --> A --> Ar
    # We are just reversing the orientation of the arrows, nothing more
    def reverse_iterative(self):
        cur = self.head
        prev = None

        while cur:
            nxt = cur.next  # Temporary variable
            cur.next = prev
            # self.print_helper(prev, "PREV")
            # self.print_helper(cur, "CUR")
            # self.print_helper(nxt, "NXT")
            print('\n')
            prev = cur
            cur = nxt
        self.head = prev

    def print_helper(self, node, name):
        if node is None:
            print(f"{name}: None")
        else:
            print(f"{name}: {node.data}")

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next  # Temporary variable
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)
        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist_2):

        # Setup
        p = self.head
        q = llist_2.head
        s = None

        # If one of the lists is null
        if not p:
            return q
        if not q:
            return p

        # make the head, (s)
        if p and q:
            if p.data <= q.data:
                s = p
                p = p.next
            else:
                s = q
                q = q.next

            new_head = s

        # Make the rest of the list until we completely cycle through either p or q
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = p.next
            else:
                s.next = q  # making pointer
                s = q  # making s equal to q
                q = q.next
        # p is finished, so just add the rest of q on
        if not p:
            s.next = q

        # q is finished, so just add the rest of p on
        if not q:
            s.next = p
        return new_head  # Return the new list















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
# llist.print_list()

# print("Now deleting node")
# llist.delete_node_position(2)
# llist.print_list()
# print(llist.length())
# print(llist.length_recursive(llist.head))

# print("Swap Nodes")
# llist.node_swap("B", "C")
# llist.reverse_iterative()
# llist.reverse_recursive()
# llist.print_list()

llist_1 = LinkedList()
llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2 = LinkedList()
llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()
