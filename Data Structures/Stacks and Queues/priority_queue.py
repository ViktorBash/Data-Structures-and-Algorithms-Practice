"""
My own implemenation of a priority queue in Python.
Input:
(data, priority)
higher priority = front of queue more
lower priority = back of queue more
LIFO
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item, priority=0):
        if self.is_empty():
            self.items.append((item, priority))
            return
        # Queue is not empty, we need to insert it in correct position
        for i in range(0, len(self.items)):
            cur_priority = self.items[i][1]  # Get the priority of current element
            if cur_priority < priority:
                self.items.insert(i, (item, priority))
                return

        self.items.append((item, priority))
        return

    def dequeue(self):
        return self.items.pop(0)[0]

    def __str__(self):
        return str(self.items)


q = Queue()

q.enqueue(5, 0)
q.enqueue(5, 2)
q.enqueue(7, 2)
q.enqueue(3, 1)
q.enqueue(10)

print(q)
print(q.dequeue())
print(q)
