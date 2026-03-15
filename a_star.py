"""A_star.ipynb
"""

import heapq

def printState(list):
  for i in range(0, 9, 3):
    for j in range(3):
        print(list[i + j], end="  ")
    print()
    
def parse_state(state_str):
    # Remove spaces and convert to a list of characters/numbers
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

def menuscript_a_star(initial_state, goal_state):

    queue = []
    entry_count = 0
    heapq.heappush(queue,(heuristic(initial_state, goal_state), 0, entry_count, initial_state,[initial_state]))
    entry_count += 1

    visited = set()
    Counter = 0

    while queue:

        f, cost, g, current_state, path  = heapq.heappop(queue) 
        Counter += 1

        if current_state == goal_state:
            return "Success", path, Counter, cost, current_state

        visited.add(current_state)


        for neighbor in get_neighbors(current_state,'B'):
            if neighbor not in visited:
                new_cost = cost + 1
                f_new = new_cost + heuristic(neighbor,goal_state)
                heapq.heappush(queue,(f_new, new_cost, entry_count, neighbor, path + [neighbor]))
                entry_count += 1

    return "Failure", None   # In case no solution


from collections import deque
import time

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
res ,path, count, cost, current_state = menuscript_a_star(initial_state, goal_state)
total_time = time.time() - start_time

print(res)
print("heuristic Parameter use is misplaced menuscript")
print("Total Cost:", cost)
print("States Explored:", count)
print("Total Time:", round(total_time, 4), "seconds")
print("Path:", path)
for step in path:
    print(step)
