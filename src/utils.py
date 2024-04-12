from .config import MAZE_SIZE
from .ref import matriz

def update_matriz(i, j, color):
    if 0 <= i < MAZE_SIZE and 0 <= j < MAZE_SIZE:
        matriz[i][j].color = color