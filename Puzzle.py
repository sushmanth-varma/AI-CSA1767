
# 1. 8-Puzzle Problem using A* algorithm
from heapq import heappop, heappush

def heuristic(state, goal):
    return sum(abs((val - 1) % 3 - (i % 3)) + abs((val - 1) // 3 - (i // 3)) for i, val in enumerate(state) if val)

def a_star(start, goal):
    frontier = []
    heappush(frontier, (0, start))
    came_from = {tuple(start): None}
    g_score = {tuple(start): 0}
    while frontier:
        _, current = heappop(frontier)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[tuple(current)]
            return path[::-1]
        neighbors = get_neighbors(current)
        for next_state in neighbors:
            temp_g_score = g_score[tuple(current)] + 1
            if tuple(next_state) not in g_score or temp_g_score < g_score[tuple(next_state)]:
                g_score[tuple(next_state)] = temp_g_score
                f_score = temp_g_score + heuristic(next_state, goal)
                heappush(frontier, (f_score, next_state))
                came_from[tuple(next_state)] = current

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    swaps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x, y = zero_idx % 3, zero_idx // 3
    for dx, dy in swaps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = state[:]
            swap_idx = ny * 3 + nx
            new_state[zero_idx], new_state[swap_idx] = new_state[swap_idx], new_state[zero_idx]
            neighbors.append(new_state)
    return neighbors

start = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
path = a_star(start, goal)
print("Path to goal:")
for p in path:
    print(p)
