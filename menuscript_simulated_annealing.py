
"""simulated_annealing.ipynb


"""

import random
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

def simulated_annealing(initial_state, goal_state, n_iterations, step_size, temp):

    current_state = initial_state
    current_engy = heuristic(initial_state, goal_state)
    best_state = current_state
    best_engy = current_engy
    scores = [best_engy]
    path = [current_state]

    for i in range(n_iterations):
        # Cooling schedule
        t = temp / float(i + 1)

        if best_engy == 0:
            break

        neighbors = get_neighbors(current_state,'B')
        n = random.choice(neighbors)
        n_engy = heuristic(n, goal_state)
        delta_E = n_engy - current_engy

        if delta_E < 0 or random.random() < math.exp(-delta_E / t):
            current_state = n
            current_engy = n_engy
            path.append(current_state)

            if current_engy < best_engy:
                best_state = current_state
                best_engy = current_engy
                scores.append(best_engy)

        if i % 500 == 0:
            print(f"Iteration {i}, Temperature {t:.3f}, Best Energy {best_engy:.5f}")



    return best_state, best_engy, scores,path

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
state, engy, score, path= simulated_annealing(initial_state, goal_state, n_iterations =10000,step_size = 0.1,temp=10)
total_time = time.time() - start_time

print("Heuristic Parameters with Misplaced Menuscript")
print("TOTAL TIME:",round(total_time, 6))
print("Best state :", state)
print("Best Enegry:", engy)
print("Minimum path:", len(path))

#print("State Explore:", i)
#if path:
    #print("Goal State :",path[-1])