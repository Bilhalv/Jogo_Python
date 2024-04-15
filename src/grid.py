"""
Creates a grid of squares to be used as a playable space.
"""
import pyglet
from pyglet import shapes
from .config import *


def find_on_grid(x, y, squares_grid):
    """
    Given an x and y coordinate, returns the row and column of the square
    that contains that coordinate. If the coordinate is not inside any
    square, it returns (None, None).
    """
    for i, row in enumerate(squares_grid):
        for j, square in enumerate(row):
            if square.x <= x <= square.x + square.width and \
                    square.y <= y <= square.y + square.height:
                return i, j
    return None, None


def update_matriz(x, y, color, matriz):
    """
    Updates the color of a square in the grid.
    """
    if x < 0 or y < 0 or x >= len(matriz) or y >= len(matriz[0]):
        return
    if color == None:
        return
    matriz[x][y].color = color

def build_labels(x, y, batch, size):
    """
    Builds labels for each square in the grid.
    """
    
    label = pyglet.text.Label(
        text=f"?",
        x=x,
        y=y + size // 2,
        batch=batch,
        color=(255, 255, 255, 255),
        width=size,
        height=size,
        font_size=SQUARE_SIZE//3,
        align="center"
    )
    
    return label

def criar_grid(lado_tela, espaco, lado_quadrado, window):
    """
    Creates a grid of squares to be used as a playable space.

    Parameters:
        lado_tela (int): length of one side of the window.
        espaco (int): space between squares in pixels.
        lado_quadrado (int): size of each square in pixels.

    Returns:
        batch (pyglet.graphics.Batch): Batch object to be rendered.
        squares_grid (list): list of lists, where each inner list is a row of
            squares.
    """
    batch = pyglet.graphics.Batch()
    label_batch = pyglet.graphics.Batch()

    # Background
    bg = shapes.Rectangle(
        x=0,
        y=0,
        width=lado_tela,
        height=lado_tela,
        color= BG_COLOR,
        batch=batch
    )

    # Grid of squares
    squares_grid = []
    labels_grid = []
    for i in range(lado_tela // (espaco + lado_quadrado)):
        squares_grid.append([])
        labels_grid.append([])
        for j in range(lado_tela // (espaco + lado_quadrado)):
            x = i * (espaco + lado_quadrado)
            y = j * (espaco + lado_quadrado)
            square = shapes.Rectangle(
                x=x,
                y=y,
                width=lado_quadrado,
                height=lado_quadrado,
                color=UNDISCOVERED_COLOR,
                batch=batch
            )
            squares_grid[i].append(square)
            labels_grid[i].append(build_labels(x, y, label_batch, lado_quadrado))
    
    return batch, squares_grid, label_batch, labels_grid
def set_label(x, y, labels, text):
    """
    Updates the text of a square in the grid.
    """
    if 0 <= x < len(labels) and 0 <= y < len(labels):
        labels[x][y].text = text
