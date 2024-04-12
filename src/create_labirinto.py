from turtle import width
import pyglet
from pyglet import shapes
from config import *
from find_on_grid import return_coords_matrix
from utils import *
from ref import isWalkable, entrance

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
    color=(0, 0, 255, 200),
)

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
    
    if isUp and isInWalkable(player.x, up):
        player.y = up
    if isDown and isInWalkable(player.x, down):
        player.y = down
    if isLeft and isInWalkable(left, player.y):
        player.x = left
    if isRight and isInWalkable(right, player.y):
        player.x = right

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
    player.draw()
        

from build_maze import build_maze

build_maze()

pyglet.app.run()