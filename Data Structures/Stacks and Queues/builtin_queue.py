"""
Using queue module to create a queue in python
"""
import queue

my_q = queue.Queue(30)

my_q.put(1)
my_q.put(2)
my_q.put(3)
my_q.put(4)
my_q.put(5)
my_q.put(6)
print(my_q)

