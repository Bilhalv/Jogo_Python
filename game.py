#Labirinto de mago
#3 itens aleatorios de inicio
#não visualização do labirinto apenas comandos de onde ir
#encontro com inimigos para gastar itens, se nao tiver, gasta vida

from src.HUD import open_hud
import pyglet # type: ignore
from pyglet import shapes   # type: ignore
from pyglet.gl import * # type: ignore
from src.config import *
from src.find_on_grid import return_coords_matrix
from src.utils import *
from src.ref import isWalkable, entrance, exit, matriz, HUD
from src.maze import build_maze

batch = pyglet.graphics.Batch()

window = pyglet.window.Window(
    SCREEN_SIZE,
    SCREEN_SIZE,
    TITLE
)

player = shapes.Circle(
    x=entrance[0]*(SQUARE_SIZE+PADDING)+(SQUARE_SIZE)/2,
    y=(SQUARE_SIZE)/2,
    radius=SQUARE_SIZE/4,
    color=(100, 0, 100, 120),
)

def show_3x3(x, y):
    matriz_volta_player = [ [x+1, y], [x, y+1], [x, y], [x, y-1], [x-1, y] ]
    for coord in matriz_volta_player:
        if coord in isWalkable and coord != entrance and coord != exit:
            update_matriz(coord[0], coord[1], color=SECUNDARY_COLOR)

def isInWalkable(x, y):
    code = return_coords_matrix(x, y, matriz)
    return code in isWalkable

@window.event
def on_key_press(symbol, modifiers):
    isUp = symbol == pyglet.window.key.UP or symbol == pyglet.window.key.W
    isDown = symbol == pyglet.window.key.DOWN or symbol == pyglet.window.key.S
    isLeft = symbol == pyglet.window.key.LEFT or symbol == pyglet.window.key.A
    isRight = symbol == pyglet.window.key.RIGHT or symbol == pyglet.window.key.D
    
    SquareSize = SQUARE_SIZE+PADDING
    
    up = player.y + SquareSize
    down = player.y - SquareSize
    left = player.x - SquareSize
    right = player.x + SquareSize
    
    if isUp or isDown or isLeft or isRight:
        if isUp and isInWalkable(player.x, up):
            player.y = up
        if isDown and isInWalkable(player.x, down):
            player.y = down
        if isLeft and isInWalkable(left, player.y):
            player.x = left
        if isRight and isInWalkable(right, player.y):
            player.x = right
        player_on_grid: list[int] = return_coords_matrix(player.x, player.y, matriz)
        show_3x3(player_on_grid[0], player_on_grid[1])

for column in range(MAZE_SIZE):
    matriz.append([])
    for row in range(MAZE_SIZE):
        rec = shapes.Rectangle(
            x=column*(SQUARE_SIZE+PADDING),
            y=row*(SQUARE_SIZE+PADDING),
            height=SQUARE_SIZE,
            width=SQUARE_SIZE,
            color=DEFAULT_COLOR,
            batch=batch
        )
        matriz[column].append(rec)

@window.event
def on_draw():
    window.clear()
    batch.draw()
    show_3x3(entrance[0], entrance[1])
    player.draw()

build_maze()

open_hud()

pyglet.app.run()