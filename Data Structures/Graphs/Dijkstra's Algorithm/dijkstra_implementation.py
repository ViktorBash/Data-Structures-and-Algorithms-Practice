"""
Implementing Dijkstra's Algorithm in Python
"""
import string


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def add_item(self, item):
        self.pq.append(item)
        self.pq.sort()
        return item

    def pop_item(self):
        return self.pq.pop(0)


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
        self.vert_dict[to_node].add_neighbor(start_node, weight)

    def get_vertices(self):
        return self.vert_dict.keys()

    def __str__(self):
        return str(self.vert_dict)

    def dijkstra(self, start_node="S"):
        for vert_name, vert in self.vert_dict.items():
            self.vert_distance[vert_name] = 999
            self.vert_prev[vert_name] = None
        self.vert_distance["S"] = 0

        self.dijkstra_util("S")

    def dijkstra_util(self, cur_node):
        start_vert = self.get_vertex(cur_node)
        for key, value in start_vert.adjacent.items():
            if self.vert_distance[key] > value:
                self.vert_prev[key] = cur_node
                self.vert_distance[key] = value

        next_node = None
        next_node_dist = 999
        for key, value in self.vert_distance.items():
            if value < next_node_dist:
                next_node = key
        print(next_node)
        self.dijkstra_util(next_node)


if __name__ == "__main__":
    g = Graph()
    g.add_vertex("S")
    alphabets = string.ascii_uppercase
    for i in range(7):
        g.add_vertex(alphabets[i])
    g.add_edge("S", "A", 8)
    g.add_edge("S", "D", 5)
    g.add_edge("S", "C", 6)
    g.add_edge("A", "D", 2)
    g.add_edge("A", "E", 1)
    g.add_edge("B", "E", 6)
    g.add_edge("D", "C", 3)
    g.add_edge("D", "F", 4)
    g.add_edge("C", "F", 9)
    g.add_edge("F", "G", 0)
    g.add_edge("G", "E", 4)
    # print(g.get_vertices())
    # print(g)
    g.dijkstra("S")
    # print(g.vert_distance)
