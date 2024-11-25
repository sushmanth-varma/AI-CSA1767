def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = [(0, 0)]
    while queue:
        state = queue.pop(0)
        if state in visited:
            continue
        if state[0] == target or state[1] == target:
            print("Solution:", state)
            return
        visited.add(state)
        queue.extend(generate_states(state, jug1, jug2))
    print("No solution")

def generate_states(state, jug1, jug2):
    a, b = state
    return [(jug1, b), (a, jug2), (0, b), (a, 0),
            (min(jug1, a + b), max(0, a + b - jug1)),
            (max(0, a + b - jug2), min(jug2, a + b))]

jug1, jug2, target = 4, 3, 2
water_jug_bfs(jug1, jug2, target)
