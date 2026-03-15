

from collections import deque
import time

def printState(list):
  for i in range(0, 9, 3):
    for j in range(3):
        print(list[i + j], end="  ")
    print()

def parse_state(str):
   
    parsed = []
    for char in str.replace(' ', ''):
        if char.isdigit():
            parsed.append(int(char))
        else:
            parsed.append(char)
    return tuple(parsed)

def get_neighbors(state, blank_space_val):
    neighbors = []

    index = state.index(blank_space_val)
    row, col = index // 3, index % 3
   
    #Move down, up, right, left
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Possible directions: down, up, right, left
    #for move in moves:
    #    print(move)
    #    for i in move:
    #      print(i)
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


def sort_menuscript_bfs(initial_state, goal_state):

    visited = set([initial_state])
    new_var = 0
    i = 0
    queue = deque([(initial_state, new_var, [initial_state])])

    while queue:

        current_state, depth, path  = queue.popleft()
        i += 1

        #print("current_state:", current_state)
        #print("goal_state:", goal_state)
        if current_state == goal_state:
            
            return "Success", depth , path , i


        for neighbor in get_neighbors(current_state,'B'):
            if neighbor not in visited:
               visited.add(neighbor)
               queue.append((neighbor, depth + 1, path + [neighbor]))
    
    return "Failure" ,None   # In case no solution


from collections import deque
import time

#initial_state = (1, 2,  3, 4,'B', 5, 6, 7, 8)
#goal_state    = (1, 2, 3, 4, 5, 6, 7, 'B', 8)

with open('input.txt', 'r') as f:
    initial_str = f.readline().strip()
    goal_str = f.readline().strip()
    
initial_state = parse_state(initial_str)
goal_state = parse_state(goal_str)

print(f"Initial State: {initial_state}")
printState(initial_state)
print(f"Goal State: {goal_state}")
printState(goal_state)

start_time = time.time()
print("start_time:", start_time)
res, moves, path, state_explore = sort_menuscript_bfs(initial_state, goal_state)

total_time = time.time() - start_time

#print("Path:", path)
print(res)
print("Number of Moves:", moves)
print("Number of State Explore:", state_explore)
print("Total Time:", round(total_time, 6))

