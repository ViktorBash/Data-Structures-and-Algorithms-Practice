"""Breadth first search in Python"""


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

        self.distance = 9999
        self.color = 'black'  # unvisited

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):  # U and v are vertices
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))

    def bfs(self, vert):
        q = []
        vert.distance = 0
        vert.color = 'red'  # Red means discovered
        for v in vert.neighbors:  # Loop through the neighbors of the starting point
            self.vertices[v].distance = vert.distance + 1  # Add 1 to the distance
            # (1 away from the starting point's distance)
            q.append(v)  # Add the neighbor to the queue

        while len(q) > 0:  # Iterating through our queue
            u = q.pop(0)  # Pop the vertex name and store it
            node_u = self.vertices[u]  # node_u is the actual vertex object
            node_u.color = 'red'  # Color to red (discovered/visited)

            for v in node_u.neighbors:  # Go through the neighbors
                node_v = self.vertices[v]  # Get the object
                if node_v.color == 'black':  # If the neighbor has not been visited, append to the queue
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:  # Set the distance
                        node_v.distance = node_u.distance + 1


def main():
    g = Graph()
    a = Vertex('A')
    g.add_vertex(a)
    g.add_vertex(Vertex('B'))
    for i in range(ord("A"), ord("K")):
        g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])

    g.bfs(a)
    g.print_graph()



if __name__ == "__main__":
    main()
