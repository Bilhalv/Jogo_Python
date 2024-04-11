import pyglet
from pyglet import shapes
from config import *
from utils import *

batch = pyglet.graphics.Batch()

window = pyglet.window.Window(
    SCREEN_SIZE,
    SCREEN_SIZE,
    TITLE
)

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
        

from build_maze import build_maze

build_maze()

pyglet.app.run()