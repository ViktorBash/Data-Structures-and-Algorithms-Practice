"""
Implementing a binary tree in Python
"""


class Node:  # Node for tree, with value, and then pointer to left and right
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# class Queue:  # For the level order transveral we utilize this queue
#     def __init__(self):
#         self.items = []
#
#     def enqueue(self, item):
#         self.items.insert(0, item)
#
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop()
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1].value
#
#     def __len__(self):
#         return self.size()
#
#     def size(self):
#         return len(self.items)


# My queue, more logical ordering with items in last place being at the end of the queue
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


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
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


class BinaryTree:  # class to make the tree
    def __init__(self, root):  # Make a root node
        self.root = Node(root)

    def print_tree(self, traversal_type):  # Print the tree with whichever transversal method
        if traversal_type.lower() == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type.lower() == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type.lower() == "postorder":
            return self.post_order_print(self.root, "")
        elif traversal_type.lower() == "levelorder":
            return self.level_order_print(self.root)
        elif traversal_type.lower() == "reverselevelorder":
            return self.reverse_level_order_print(self.root)
        else:
            print("Traversal type not supported")
            return False

    def preorder_print(self, start, traversal):
        # Root -> Left -> Right
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        # Left -> Right-> Root
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def level_order_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    @staticmethod
    def reverse_level_order_print(start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        stack = Stack()
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

        return size

    def size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)


def main():

    # Demonstrating creating and traversing a tree
    # tree = BinaryTree(1)
    # tree.root.left = Node(2)
    # tree.root.right = Node(3)
    # tree.root.left.left = Node(4)
    # tree.root.left.right = Node(5)
    # tree.root.right.left = Node(6)
    # tree.root.right.right = Node(7)
    # tree.root.right.right.right = Node(8)
    # print(tree.print_tree("preorder"))
    # print(tree.print_tree("inorder"))
    # print(tree.print_tree("postorder"))

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    # print(tree.print_tree("levelorder"))
    print(tree.print_tree("reverselevelorder"))
    # print(tree.height(tree.root))
    print(tree.size())
    print(tree.size_recursive(tree.root))


if __name__ == "__main__":
    main()
