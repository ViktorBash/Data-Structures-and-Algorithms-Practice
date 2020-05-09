"""
Linked lists in python.
Linked list are not built in (we have to make it ourselves).

linked lists have nodes where a data piece and a pointer to the next list.
The pointer is the memory address of the next node.
The head is the initial pointer, and the last pointer is set to NULL.

There are multiple types of linked lists, the simplest is single linked list where there are pointer in one direction.
There is also double linked list (pointers both ways) and circular where a linked list can loop.
https://www.youtube.com/watch?v=JlMyYuY1aXU&list=PLEJyjB1oGzx3iTZvOVedkT8nZ2cG105U7&index=2
4:10

The head node will never contain any data and will not be indexable.


We make our class node where we have data and the next element. Then the linked_list class makes a head in the init
function.
The append function adds a new node by iterating to the end with a while loop.
The length function gets the len of the linked list by iterating to the end with a while loop.
Display just gets the linked list into a list and prints it.
The get function finds the element at a certain index.

"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR, index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR, Index out of range")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def count(self, data):
        cur_node = self.head
        amount = 0
        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_node.data == data:
                amount += 1
        return amount


my_list = linked_list()
# my_list.append(1)
# my_list.append(2)
# my_list.display()
# # Printing the index of element
# print(my_list.get(1))
# my_list.erase(1)
# my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(1)
my_list.display()
print("Counting amount of instances")
print(my_list.count(1))
