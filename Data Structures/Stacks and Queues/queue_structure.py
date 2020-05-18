"""
Implementing a queue in python.
FIFI, first in first out, like queue in real life

Functions;
is empty: check if the queue is empty
enqueue: adding element into array (at the end)
dequeue: remove element from the array (first element)
size: get size of queue
__str__: print out the queue
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0].value


def main():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    print(my_queue)

    my_queue.dequeue()
    my_queue.dequeue()
    print(my_queue)


if __name__ == "__main__":
    main()