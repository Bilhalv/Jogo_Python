"""
Creates a grid of squares to be used as a playable space.
"""
import pyglet
from pyglet import shapes


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
    matriz[x][y].color = color


def criar_grid(lado_tela, espaco, lado_quadrado):
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

    # Background
    bg = shapes.Rectangle(
        x=0,
        y=0,
        width=lado_tela,
        height=lado_tela,
        color=(0, 0, 0),
        batch=batch
    )

    # Grid of squares
    squares_grid = []
    for i in range(lado_tela // (espaco + lado_quadrado)):
        squares_grid.append([])
        for j in range(lado_tela // (espaco + lado_quadrado)):
            square = shapes.Rectangle(
                x=i * (espaco + lado_quadrado),
                y=j * (espaco + lado_quadrado),
                width=lado_quadrado,
                height=lado_quadrado,
                color=(255, 255, 255, 155),
                batch=batch
            )
            squares_grid[i].append(square)

    return batch, squares_grid
