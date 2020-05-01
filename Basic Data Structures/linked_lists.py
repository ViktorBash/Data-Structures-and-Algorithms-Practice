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
"""


class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
