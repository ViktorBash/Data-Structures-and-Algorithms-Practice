"""
Detecting bridges in a graph in Python.
***Not finished***
"""


class Vertex:
    def __init__(self, node):
        self.id = node
        self.neighbors = []

    def add_neighbor(self, neighbor):
        return self.neighbors.append(neighbor)

    def get_neighbors(self):
        return self.neighbors

    def get_id(self):
        return self.id


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.id = 0

        self.ids = [0 for n in range(len(self.vert_dict))]
        self.low = [0 for n in range(len(self.vert_dict))]
        self.visited = [False for n in range(len(self.vert_dict))]

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        return None

    def add_edge(self, start_node, to_node):
        if start_node not in self.vert_dict or to_node not in self.vert_dict:
            return None
        self.vert_dict[start_node].add_neighbor(to_node)
        return
        # Uncomment if you want undirected graph
        # self.vert_dict[to_node].add_neighbor(start_node, weight)

    def get_vertices(self):
        return self.vert_dict.keys()

    def __str__(self):
        return str(self.vert_dict)

    def find_bridges(self):
        self.bridges = []
        for a in range(len(self.vert_dict)):
            if not self.visited[a]:
                self.depth_first_search(a, -1, self.bridges)
        return self.bridges

    def depth_first_search(self, at, parent, bridges):
        self.visited[at] = True
        self.id += 1
        self.low[at] = self.ids[at] = self.id

        for neighbor_name in self.vert_dict[at].neighbors:
            if int(neighbor_name) == parent:
                continue
            if not self.visited[int(neighbor_name)]:
                self.depth_first_search(int(neighbor_name), at, bridges)
                self.low[at] = min(self.low[at], self.low[int(neighbor_name)])
                if self.ids[at] < self.low[int(neighbor_name)]:
                    self.bridges.append(at)
                    self.bridges.append(int(neighbor_name))
            else:
                self.low[at] = min(self.low[at], self.ids[int(neighbor_name)])


if __name__ == "__main__":
    g = Graph()
    for i in range(0, 9):
        g.add_vertex(str(i))
    g.add_edge("0", "1")
    g.add_edge("1", "2")
    g.add_edge("2", "0")

    g.add_edge("2", "3")
    g.add_edge("3", "4")

    g.add_edge("2", "5")
    g.add_edge("5", "6")
    g.add_edge("6", "7")
    g.add_edge("7", "8")
    g.add_edge("8", "5")
    g.find_bridges()
    print(g.bridges)
