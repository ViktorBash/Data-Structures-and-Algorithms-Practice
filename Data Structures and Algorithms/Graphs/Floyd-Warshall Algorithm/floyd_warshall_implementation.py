"""
Floyd-Warshall Implementation in Python
"""
INF = float('inf')  # What we will use to represent infinity


# Print the graph nicely
def print_helper(graph_to_print):
    length = len(graph_to_print)
    for graph in range(length):
        print(f"Matrix: {graph}")
        for row in range(length - 1):
            print(graph_to_print[graph][row])
        print("")
    return graph_to_print


# Main algorithm to do floyd_warshall, takes in matrix of edges as input
def floyd_warshall(graph):
    N = len(graph)
    final_solution = [graph]

    for k in range(1, N+1):
        prev_solution = final_solution[k-1]
        cur_solution = []

        for a in range(4):
            cur_solution.append([])
            for b in range(4):
                cur_solution[a].append(5)

        for i in range(N):
            for j in range(N):
                cur_solution[i][j] = min(prev_solution[i][j], prev_solution[i][k-1] + prev_solution[k-1][j])
        final_solution.append(cur_solution)

    return print_helper(final_solution)


if __name__ == "__main__":
    print("FLOYD WARSHALL ALGORITHM")
    print("")
    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
             ]
    floyd_warshall(graph)