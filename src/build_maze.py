"""
Function to build a maze using the recursive backtracking algorithm.

Parameters:
    isWalkable (list): list of walkable coordinates
    entrance (list): coordinates of the entrance
    exit (list): coordinates of the exit
    matriz (list): grid of squares

Returns:
    None
"""
import random
from .config import *
from .grid import set_label, update_matriz
MAZE_SIZE = global_.DIFICULDADE_ATUAL

def build_maze(isWalkable, entrance, exit, matriz, labels):
    """Recursive backtracking algorithm to build a maze"""
    def num_adjacent_walkables(x, y):
        """Count number of walkable neighbors"""
        adjacent_coords = [
            [x-1, y], [x+1, y], [x, y-1], [x, y+1], 
            [x-1, y-1], [x+1, y-1], [x-1, y+1], [x+1, y+1]
        ]
        return sum(1 for coord in adjacent_coords if coord in isWalkable)

    current = entrance

    while True:
        # Check if we've reached the exit
        if current == exit:
            break

        # Generate all possible moves
        N = [current[0], current[1] + 1]
        S = [current[0], current[1] - 1]
        E = [current[0] + 1, current[1]]
        W = [current[0] - 1, current[1]]
        options = [c for c in [N, S, E, W]
                   if 0 <= c[0] < MAZE_SIZE and 0 <= c[1] < MAZE_SIZE
                   and num_adjacent_walkables(c[0], c[1]) <= 3
                   and c not in isWalkable]

        # If we have no options, backtrack
        if not options:
            isWalkable.pop()
            if not isWalkable:
                current = entrance
            else:
                current = random.choice(isWalkable)

        # If we have options, choose one and update the list of walkable coords
        else:
            random.shuffle(options)
            current = options[0]
            isWalkable.append(current)

    # Update colors of the starting and ending points
    update_matriz(exit[0], exit[1], EXIT_COLOR, matriz=matriz)
    update_matriz(entrance[0], entrance[1], ENTRANCE_COLOR, matriz=matriz)
    set_label(entrance[0], entrance[1], labels, "Start")
    set_label(exit[0], exit[1], labels, "End")

