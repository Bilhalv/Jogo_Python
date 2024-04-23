import random
from .config import *
from .grid import Grid

def build_maze(grid:Grid):
    """Recursive backtracking algorithm to build a maze"""
    def num_adjacent_walkables(x, y):
        """Count number of walkable neighbors"""
        adjacent_coords = [
            [x-1, y], [x+1, y], [x, y-1], [x, y+1], 
            [x-1, y-1], [x+1, y-1], [x-1, y+1], [x+1, y+1]
        ]
        return sum(1 for coord in adjacent_coords if grid._get_square(coord).color == FLOOR_COLOR)

    current = grid.entrance

    while True:
        # Check if we've reached the exit
        if current == grid.exit:
            break

        # Generate all possible moves
        N = [current[0], current[1] + 1]
        S = [current[0], current[1] - 1]
        E = [current[0] + 1, current[1]]
        W = [current[0] - 1, current[1]]
        options = [c for c in [N, S, E, W]
                   if 0 <= c[0] < global_.DIFICULDADE_ATUAL and 0 <= c[1] < global_.DIFICULDADE_ATUAL
                   and num_adjacent_walkables(c[0], c[1]) <= 3
                   and grid._get_square(c).color == FLOOR_COLOR]

        # If we have no options, backtrack
        if not options:
            if not grid._get_walkable_coords():
                current = grid.entrance
            else:
                current = random.choice(grid._get_walkable_coords())

        # If we have options, choose one and update the list of walkable coords
        else:
            random.shuffle(options)
            current = options[0]
            grid._set_walkable_coords(grid._get_walkable_coords.append(current))
