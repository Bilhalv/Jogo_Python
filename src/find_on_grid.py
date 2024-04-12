from .config import MAZE_SIZE, SQUARE_SIZE
from .ref import matriz

def return_coords_matrix(x, y, matriz):
    return_x = 0
    return_y = 0
    for i in range(MAZE_SIZE):
        for j in range(MAZE_SIZE):
            if matriz[i][j].x <= x and x <= matriz[i][j].x+SQUARE_SIZE and matriz[i][j].y <= y and y <= matriz[i][j].y+SQUARE_SIZE:
                return_x = i
                return_y = j
    return [return_x, return_y]
