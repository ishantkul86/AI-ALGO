

import math

def printState(list):
  for i in range(0, 9, 3):
    for j in range(3):
        print(list[i + j], end="  ")
    print()
    
def parse_state(state_str):
    parsed = []
    for char in state_str.replace(' ', ''):
        if char.isdigit():
            parsed.append(int(char))
        else:
            parsed.append(char)
    return tuple(parsed)

def heuristic(state, goal_state):
    count = 0
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if state[index] != 'B' and state[index] != goal_state[index]:
                count += 1
    return count

def get_neighbors(state, blank_space_val):
    neighbors = []

    index = state.index(blank_space_val)
    row, col = index // 3, index % 3


    #Move down, up, right, left
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


    for row_change, column_change in moves:
        new_row = row + row_change
        new_col = col + column_change

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)

            temp = new_state[index]
            new_state[index] = new_state[new_index]
            new_state[new_index] = temp

            neighbors.append(tuple(new_state))


    return neighbors

def minimax(initial_state, goal_state, depth, is_max):
    global nodes_minimax
    nodes_minimax += 1
    if initial_state == goal_state or depth == 0:
      return 10000 if initial_state==goal_state else -heuristic(initial_state, goal_state)
    if is_max:
        return max(minimax(neighbor, goal_state, depth-1, False) for neighbor in get_neighbors(initial_state, 'B'))
    else:
        return min(minimax(neighbor, goal_state, depth-1, True) for neighbor in get_neighbors(initial_state, 'B'))

def alphabeta(initial_state, goal_state,depth, is_max, alpha, beta):
    global nodes_ab
    nodes_ab += 1
    if initial_state == goal_state or depth == 0:
       return 10000 if initial_state==goal_state else  -heuristic(initial_state, goal_state)
    if is_max:
        max_eval = -math.inf
        for neighbor in get_neighbors(initial_state, 'B'):
            eval = alphabeta(neighbor, goal_state, depth-1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # prune
        return max_eval
    else:
        min_eval = math.inf
        for neighbor in get_neighbors(initial_state, 'B'):
            eval = alphabeta(neighbor, goal_state, depth-1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # prune
        return min_eval

# Run plain Minimax
# Node counters

with open('input.txt', 'r') as f:
    initial_str = f.readline().strip()
    goal_str = f.readline().strip()
    
initial_state = parse_state(initial_str)
goal_state = parse_state(goal_str)

print(f"Initial State: {initial_state}")
printState(initial_state)
print(f"Goal State: {goal_state}")
printState(goal_state)


nodes_minimax = 0
nodes_ab = 0
#initial_state = (1, 2,  3, 4,'B', 5, 6, 7, 8)
#goal_state    = (1, 2, 3, 4, 5, 6, 7, 'B', 8)
nodes_minimax = 0
minimax(initial_state, goal_state, depth=4, is_max=True )

nodes_ab = 0
alphabeta(initial_state,goal_state, depth=4, is_max=True, alpha=-math.inf, beta=math.inf)
print("alphabeta pruning:", nodes_ab)
print("plain Minimax:", nodes_minimax)

