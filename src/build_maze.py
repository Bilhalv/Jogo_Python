import random
from config import *
from utils import *
from ref import *

def build_maze():
    
    current = entrance
    
    while True:
        if current == exit:
            break
        N = [current[0], current[1] + 1]
        S = [current[0], current[1] - 1]
        E = [current[0] + 1, current[1]]
        W = [current[0] - 1, current[1]]

        # Filter out options that have too many walkable neighbors
        options = [
            coord for coord in [N, S, E, W]
            if 0 <= coord[0] < MAZE_SIZE and 0 <= coord[1] < MAZE_SIZE
            and num_adjacent_walkables(coord[0], coord[1]) <= 2
            and coord not in isWalkable
        ]
        
        random.shuffle(options)
        
        if len(options) >= 1:
            current = options[0]
            isWalkable.append(current)
            
        else:
            isWalkable.pop()
            if len(isWalkable) == 0:
                current = entrance
            else:
                current = random.choice(isWalkable)
    for walk in isWalkable:
        update_matriz(walk[0], walk[1], color=SECUNDARY_COLOR)
    update_matriz(exit[0], exit[1], color=EXIT_COLOR)
    update_matriz(entrance[0], entrance[1], color=EXIT_COLOR)
    
def num_adjacent_walkables(x, y):
    adjacent_coords = [
        [x-1, y], [x+1, y], [x, y-1], [x, y+1], 
        [x-1, y-1], [x+1, y-1], [x-1, y+1], [x+1, y+1]
    ]
    soma = 0
    for coord in adjacent_coords:
        if coord in isWalkable:
            soma += 1
    return soma
