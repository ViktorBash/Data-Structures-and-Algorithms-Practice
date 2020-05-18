"""
Depth first search in Python
"""


# This is the class to make our nodes, with the node data and a direction to go to
# class AdjNode:
#     def __init__(self, data):
#         self.vertex = data
#         self.next = None


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:  # If is not already a neighbor
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}  # Dict to hold vertice names keyed to objects
    time = 0

    def add_vertex(self, vertex):
        # Check if the vertex we passed in is actually a Vertex
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
