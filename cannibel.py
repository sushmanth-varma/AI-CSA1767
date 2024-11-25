class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = None

def is_valid(state):
    if state.missionaries < 0 or state.cannibals < 0 or state.missionaries > 3 or state.cannibals > 3:
        return False
    if state.missionaries > 0 and state.missionaries < state.cannibals:
        return False
    if 3 - state.missionaries > 0 and 3 - state.missionaries < 3 - state.cannibals:
        return False
    return True

def bfs(initial_state):
    queue = [initial_state]
    visited = set()
    while queue:
        current_state = queue.pop(0)
        if current_state.missionaries == 0 and current_state.cannibals == 0 and current_state.boat == 0:
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return path[::-1]
        visited.add((current_state.missionaries, current_state.cannibals, current_state.boat))
        next_states = generate_next_states(current_state)
        for state in next_states:
            if (state.missionaries, state.cannibals, state.boat) not in visited and is_valid(state):
                state.parent = current_state
                queue.append(state)
def generate_next_states(state):
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
    next_states = []
    if state.boat == 1:
        for m, c in moves:
            next_states.append(State(state.missionaries - m, state.cannibals - c, 0))
    else:
        for m, c in moves:
            next_states.append(State(state.missionaries + m, state.cannibals + c, 1))
    return next_states

initial_state = State(3, 3, 1)
solution = bfs(initial_state)
if solution:
    for s in solution:
        print(f"Missionaries: {s.missionaries}, Cannibals: {s.cannibals}, Boat: {s.boat}")
else:
    print("No solution found")
