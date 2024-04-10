import pyglet
import random
from pyglet import shapes
from config import *

matriz = []
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

isWalkable = []

def build_maze():
    print("Building Maze..")
    saida = [MAZE_SIZE-1, MAZE_SIZE-1]
    update_matriz(saida[0], saida[1], EXIT_COLOR)
    entrada = [0, 0]
    update_matriz(entrada[0], entrada[1], EXIT_COLOR)
    isWalkable.append(entrada)
    i = 0
    while True:
        LocalTemp = isWalkable[i]
        caminhos = []
        def run(new:list):
            if not new in isWalkable:
                caminhos.append(new)
        if 0 <= LocalTemp[0]+1 < MAZE_SIZE:
            new = [LocalTemp[0]+1, LocalTemp[1]]
            run(new)
        if 0 <= LocalTemp[0]-1 < MAZE_SIZE:
            new = [LocalTemp[0]-1, LocalTemp[1]]
            run(new)
        if 0 <= LocalTemp[1]+1 < MAZE_SIZE:
            new = [LocalTemp[0], LocalTemp[1]+1]
            run(new)
        if 0 <= LocalTemp[1]-1 < MAZE_SIZE:
            new = [LocalTemp[0], LocalTemp[1]-1]
            run(new)
        if len(caminhos) > 0:
            LocalTemp = caminhos[random.randrange(0, len(caminhos))]
            if LocalTemp == saida:
                break
            isWalkable.append(LocalTemp)
        else:
            LocalTemp = random.randrange(1, MAZE_SIZE), random.randrange(1, MAZE_SIZE)
            if LocalTemp == saida:
                break
            isWalkable.append(LocalTemp)
        update_matriz(LocalTemp[0], LocalTemp[1], SECUNDARY_COLOR)
        i += 1
        

def update_matriz(i, j, color):
    if 0 <= i < MAZE_SIZE and 0 <= j < MAZE_SIZE:
        matriz[i][j].color = color
        return

build_maze()

pyglet.app.run()