from config import *

def return_coords_matrix(x, y, matriz):
    for i in range(MAZE_SIZE):
        for j in range(MAZE_SIZE):
            if matriz[i][j].x <= x and x <= matriz[i][j].x+SQUARE_SIZE and matriz[i][j].y <= y and y <= matriz[i][j].y+SQUARE_SIZE:
                return [i, j]
