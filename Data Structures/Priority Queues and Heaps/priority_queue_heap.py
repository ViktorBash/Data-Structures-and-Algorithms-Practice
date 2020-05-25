"""
Creating a Priority Queue via a heap
This will be a minheap (good for Dijkstra's algorithm)
"""


class PriorityQueue:
    def __init__(self):
        self.items = [None, 3, 5, 4, 10, 8, 6]

    def parent(self, pos):
        if pos == 0:
            return None
        return pos // 2

    def left_child(self, pos):
        if 2 * pos > len(self.items):
            return None
        return 2 * pos

    def right_child(self, pos):
        if (2 * pos + 1) > len(self.items):
            return None
        return 2 * pos + 1

    def insert(self, num):
        # If no list, just insert as start
        if len(self.items) == 1:
            return self.items.append(num)

        # Append the num, then we will swap/sort
        self.items.append(num)
        # Get position of parent and create bool
        parent_item = self.parent(len(self.items)-1)
        break_loop = False

        print(self.items)
        # While we are not at the start node
        while parent_item > 0 and not break_loop:
            # Initialize values to compare, (we swap indices and compare values)
            try:
                left_child_val = self.items[self.left_child(parent_item)]
            except IndexError:
                left_child_val = None
            try:
                right_child_val = self.items[self.right_child(parent_item)]
            except IndexError:
                right_child_val = None
            parent_val = self.items[parent_item]

            # Swap if right child is less than parent
            if right_child_val is not None:
                # Right child is less than minheap
                if right_child_val < parent_val:
                    self.swap_nodes(parent_item, self.right_child(parent_item))
            # Swap if left child is less than parent (only if we didn't swap before)
            elif left_child_val is not None:
                if left_child_val < parent_val:
                    self.swap_nodes(parent_item, self.left_child(parent_item))

            # Iterate through (change parent)
            parent_item = self.parent(parent_item)
            print(self.items)

    # Takes in 2 indices to swap values
    def swap_nodes(self, num1, num2):
        self.items[num1], self.items[num2] = self.items[num2], self.items[num1]


q = PriorityQueue()
q.insert(1)
