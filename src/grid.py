import pyglet
from pyglet import shapes

def find_on_grid(x, y, squares_grid):
    row, column = 0, 0
    for i in range(len(squares_grid)):
        for j in range(len(squares_grid)):
            if squares_grid[i][j].x <= x and x <= squares_grid[i][j].x+squares_grid[i][j].width and squares_grid[i][j].y <= y and y <= squares_grid[i][j].y+squares_grid[i][j].height:
                row = i
                column = j
    return [row, column]

def update_matriz(x, y, color, matriz):
    matriz[x][y].color = color

def criar_grid(lado_tela, espaco, lado_quadrado):
    batch = pyglet.graphics.Batch()
    bg = shapes.Rectangle(
        x=0,
        y=0,
        width=lado_tela, 
        height=lado_tela,
        color=(0, 0, 0),
        batch=batch
    )
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