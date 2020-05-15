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

    def __len__(self):
        return self.items.__len__()


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str


def main():
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

    reverse_str = Stack()
    print(reverse_string(reverse_str, "Hello"))


if __name__ == "__main__":
    main()
