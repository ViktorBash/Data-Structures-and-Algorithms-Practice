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
        # Our vertex has name, list of neighbors, and some other attributes
        self.name = name
        self.neighbors = []

        self.discovery = 0  # When we discovery the vertex
        self.finish = 0  # When we go back and finish
        self.color = 'black'

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:  # If is not already a neighbor
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}  # Dict to hold vertice names keyed to objects
    time = 0

    def add_vertex(self, vertex):  # Add vertex to our graph
        # Check if the vertex we passed in is actually a Vertex and is not already in the dictionary
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):  # Takes 2 character values, (2 vertices)
        if u in self.vertices and v in self.vertices:  # If v and u are existing vertices
            for key, value in self.vertices.items():  # iterate through and add neighbor to both u and v
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):  # Print info about the graph
        for key in sorted(list(self.vertices.keys())):
            print(f"{key} {str(self.vertices[key].neighbors)} {str(self.vertices[key].discovery)} / {str(self.vertices[key].finish)}")

    def _dfs(self, vertex):
        global time
        vertex.color = 'red'  # Already discovered
        vertex.discovery = time  # When we discover the vertex, we add the timestamp to it as an attribute
        time += 1  # Increment time
        for v in vertex.neighbors:  # Go through the list of neighbors (recursion) to do the same steps
            if self.vertices[v].color == 'black':  # black means it has not been visited yet
                self._dfs(self.vertices[v])

        # After the for loop, we have explored the nodes past the vertex, and have backtracked back with recursion
        # Now we have explored everything past the current vertex, so we go back and set the vertex to blue
        # To show that
        vertex.color = 'blue'  # Finished
        # print(vertex.name)
        vertex.finish = time  # Set finish time
        time += 1  # Increment time

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)


def main():
    g = Graph()  # Create graph
    a = Vertex('A')  # Create vertex
    g.add_vertex(a)  # add vertex to the graph
    g.add_vertex(Vertex('B')) # another way to add vertex to the graph in one line

    for i in range(ord('A'), ord('K')):  # Add vertexes from range a to j (k non inclusive)
        # A and B will not add again because we have a check for them
        g.add_vertex(Vertex(chr(i)))  # Add vertex

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])  # Adds the edges to the add edge function and neighbors list

    g.dfs(a)
    g.print_graph()  # This prints what DFS found


if __name__ == "__main__":
    main()