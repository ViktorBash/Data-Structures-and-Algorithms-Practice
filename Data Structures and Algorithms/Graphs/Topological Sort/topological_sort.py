"""
Topological sort algorithm in Python
"""

from collections import defaultdict

# Dictionary with node_name keyed to a list of it's neighbors
adjacency_list = defaultdict()
adjacency_list['a'] = ['d']
adjacency_list['b'] = ['d']
adjacency_list['c'] = ['e']
adjacency_list['d'] = ['e']
adjacency_list['e'] = []

# Dictionary with node name keyed to a boolean statement (whether is has been visited or not)
visited_list = defaultdict()
visited_list['a'] = False
visited_list['b'] = False
visited_list['c'] = False
visited_list['d'] = False
visited_list['e'] = False

# We will print the output stack to get our result
output_stack = []


def topology_sort(vertex):  # Take in initial vertex
    if not visited_list[vertex]:  # If the vertex is already visited, then we end the function
        visited_list[vertex] = True  # Set visited to true
        for neighbor in adjacency_list[vertex]:  # Go through it's neighbors
            topology_sort(neighbor)
        output_stack.insert(0, vertex)  # This is a stack, so we insert at 0 instead of appending (stack of plates)


for vertex in visited_list:  # Input every single vertex into the topology_sort function
    topology_sort(vertex)

print(output_stack)