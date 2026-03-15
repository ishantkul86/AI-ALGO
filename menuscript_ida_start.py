
"""IDA_Start.ipynb
"""


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

def menuscript_ida_star(initial_state, goal_state):

    threshold = heuristic(initial_state, goal_state)
    i = 0

    while True:
        path =[initial_state]
        tmp , nodes_check= search_ida(initial_state,  goal_state, 0,threshold,path )

        i += nodes_check

        if tmp == True:
            return True, threshold, path, i
        elif tmp == float('inf'):
            return False, threshold, path,  i
        else:
            threshold = tmp

def search_ida(current_state, goal_state, g, threshold, path):

    count_nodes =1
    f = g + heuristic(current_state, goal_state)

    if f > threshold:
        return f, count_nodes

    if current_state == goal_state:
        return True, count_nodes

    minimum = float('inf')
    for n in get_neighbors(current_state,'B'):
        if n not in path:
            path.append(n)
            tmp, count = search_ida(n, goal_state, g + 1, threshold, path)
            count_nodes += count
            if tmp == True:
                return True,count_nodes
            if tmp < minimum:
                minimum = tmp

    return minimum , count_nodes

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

#initial_state = (1, 2,  3, 4,'B', 5, 6, 7, 8)
#goal_state    = (1, 2, 3, 4, 5, 6, 7, 'B', 8)
start_time = time.time()
result, threshold, path, i = menuscript_ida_star(initial_state, goal_state)
total_time = time.time() - start_time

if result:
    print("Success")
else:
    print("Failure")

print("Heuristic Parameters with Misplaced Menuscript")
print("States Explored:", i)
print("Threshold :", threshold)

print("Total Time:", round(total_time, 6), "seconds")
print("Path:", path)

if path:
    print("Goal State :",path[-1])
#if path:
        #for step, state in enumerate(path):
            #print(f"Step {step}: {state}")
#print("Current state:", current_state)

#print("Optimal Path:", path)
#print("Total Cost:", len(path) - 1)