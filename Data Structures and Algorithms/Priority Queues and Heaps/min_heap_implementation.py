"""
Making a min heap in Python
"""

import sys


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        # self.Heap = [0]*(self.maxsize + 1)
        self.Heap = [0 for n in range(maxsize + 1)]
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    def swap(self, fpos, pos):
        self.Heap[fpos], self.Heap[pos] = self.Heap[pos], self.Heap[fpos]

    # Heapify the node we put in (make the heap correct after we change something)
    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                    # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

            # Function to print the contents of the heap

    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

            # Function to build the min heap using

    # the minHeapify function
    def minHeap(self):

        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

            # Function to remove and return the minimum

    # element from the heap
    def remove(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped

    # Driver Code


if __name__ == "__main__":
    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()

    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
