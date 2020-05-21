"""
My own implementation of top-sort in Python
"""

adjacency_list = {'a': ['d'], 'b': ['d'], 'c': ['e'], 'd': ['e'], 'e': []}
# print(adjacency_list)

ordering_stack = []
visited = set()


def topology_sort(adjancency_list):
    for key, value in adjacency_list.items():
        topology_helper(key)
    return ordering_stack


def topology_helper(vertex):
    if vertex not in visited:
        visited.add(vertex)
        for neighbor in adjacency_list[vertex]:
            topology_helper(neighbor)
        ordering_stack.insert(0, vertex)


print(topology_sort(adjacency_list))
