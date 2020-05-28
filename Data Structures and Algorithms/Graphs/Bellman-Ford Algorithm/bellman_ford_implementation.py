"""
Implementing bellman ford algorithm in Python
"""


import string


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.vert_distance = {}
        self.vert_prev = {}

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        return None

    def add_edge(self, start_node, to_node, weight=0):
        if start_node not in self.vert_dict or to_node not in self.vert_dict:
            return None
        self.vert_dict[start_node].add_neighbor(to_node, weight)
        # If we want undirected graph uncomment this line out, otherwise we will be making it directed
        # self.vert_dict[to_node].add_neighbor(start_node, weight)

    def get_vertices(self):
        return self.vert_dict.keys()

    def __str__(self):
        return str(self.vert_dict)

    def bellman_ford(self, start_node="S"):
        for vert_name, vert in self.vert_dict.items():
            self.vert_distance[vert_name] = 999
            self.vert_prev[vert_name] = None
        self.vert_distance["S"] = 0
        self.bellman_ford_util()

    def bellman_ford_util(self):
        for i in range(len(self.vert_dict) - 1):
            for vert_name, vert in self.vert_dict.items():
                for vert_name_neighbor, edge in vert.adjacent.items():
                    if self.vert_distance[vert_name_neighbor] > edge + self.vert_distance[vert_name]:
                        self.vert_distance[vert_name_neighbor] = edge + self.vert_distance[vert_name]
                        self.vert_prev[vert_name_neighbor] = vert_name
        print(self.vert_distance)
        print(self.vert_prev)


if __name__ == "__main__":
    g = Graph()
    g.add_vertex("S")
    alphabets = string.ascii_uppercase
    for i in range(8):
        g.add_vertex(alphabets[i])
    g.add_edge("S", "A", 2)
    g.add_edge("A", "E", -3)
    g.add_edge("E", "B", 1)
    g.add_edge("B", "C", 7)
    g.add_edge("C", "F", -5)
    g.add_edge("F", "B", 8)
    g.add_edge("E", "H", -3)
    g.add_edge("E", "G", 6)
    g.add_edge("H", "G", 1)
    g.add_edge("G", "D", 2)
    g.bellman_ford("S")

