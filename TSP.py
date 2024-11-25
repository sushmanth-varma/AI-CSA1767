from itertools import permutations

def tsp(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')
    best_route = []

    for perm in permutations(vertices):
        current_cost = 0
        current_path = [start] + list(perm) + [start]

        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i + 1]]

        if current_cost < min_path:
            min_path = current_cost
            best_route = current_path

    return best_route, min_path

# Example weighted graph for TSP
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

best_route, min_cost = tsp(graph, 'A')
print("TSP Best Route:", best_route)
print("TSP Minimum Cost:", min_cost)
