"""
Stack in python
Put something on the stack: Push
Take something off the stack: Pop
Operations done on the top of the stack (by definition of what a stack is)
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):  # Get the first item in the stack, (the one that will be popped first)
        if not self.is_empty():
            return self.items[-1]


# The top of the stack if the right, or index -1.
s = Stack()
# s.push("A")
# s.push("B")
# print(s.get_stack())
# s.push("C")
# s.pop()
# s.pop()
# print(s.get_stack())
# print(s.is_empty())

s.push("A")
s.push("B")
s.push("C")
s.push("D")
print(s.get_stack())
print(s.peek())
