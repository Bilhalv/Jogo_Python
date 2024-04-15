import pyglet
from src.HUD.index import *
from src.config import *
from src.grid import criar_grid
from src.build_maze import build_maze
from src.player import *

"""
Main window
"""
window = pyglet.window.Window(SCREEN_SIZE, SCREEN_SIZE+MENU_SIZE, "Labirinto do mago!")

"""
Grid of squares
"""
quadrados_batch, quadrados, label_batch, labels = criar_grid(SCREEN_SIZE, PADDING, SQUARE_SIZE, window)

"""
Start and end coordinates
"""
entrada = [0, SCREEN_SIZE//(SQUARE_SIZE+PADDING)-1]
saida = [SCREEN_SIZE//(SQUARE_SIZE+PADDING)-1, 0]

"""
List of walkable coordinates
"""
andaveis = []

"""
Player's initial coordinates
"""
player_coord = [entrada[0]*(SQUARE_SIZE+PADDING)+(SQUARE_SIZE)/2, entrada[1]*(SQUARE_SIZE+PADDING)+(SQUARE_SIZE)/2]

# build the maze
build_maze(andaveis, entrada, saida, quadrados, labels)

# create player
player = build_player(SQUARE_SIZE//4, player_coord)

# show the starting positions
show_3x3(entrada[0], entrada[1], andaveis, quadrados, entrada, saida, labels)
andaveis.append(entrada)
andaveis.append(saida)

@window.event
def on_key_press(symbol, modifiers):
    """
    Handle player movement
    """
    move_player(player=player, andaveis=andaveis, quadrados=quadrados, entrada=entrada, saida=saida, key=symbol, sqr=SQUARE_SIZE+PADDING, window=window, labels=labels)
    if symbol == pyglet.window.key.ESCAPE:
        exit()
    if symbol == pyglet.window.key.SPACE:
        start()
    if symbol == pyglet.window.key.R:
        restart()

def restart():
    """
    Restarts the game.
    """
    global andaveis, quadrados, player, quadrados_batch
    andaveis = []
    quadrados_batch, quadrados, label_batch, labels = criar_grid(SCREEN_SIZE, PADDING, SQUARE_SIZE, window)
    build_maze(andaveis, entrada, saida, quadrados, labels)
    show_3x3(entrada[0], entrada[1], andaveis, quadrados, entrada, saida, labels)
    andaveis.append(entrada)
    andaveis.append(saida)
    player_coord = [entrada[0]*(SQUARE_SIZE+PADDING)+(SQUARE_SIZE)/2, entrada[1]*(SQUARE_SIZE+PADDING)+(SQUARE_SIZE)/2]
    player = build_player(SQUARE_SIZE//4, player_coord)

def exit():
    """
    Exits the game.
    """
    window.close()

def start():
    """
    Starts the game.
    """
    global andaveis, quadrados, player, quadrados_batch
    player_coord = [entrada[0]*(SQUARE_SIZE+PADDING)+(SQUARE_SIZE)/2, entrada[1]*(SQUARE_SIZE+PADDING)+(SQUARE_SIZE)/2]
    player = build_player(SQUARE_SIZE//4, player_coord)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if isStart(x, y):
        start()

    elif isRestart(x, y):
        restart()

@window.event
def on_draw():
    """
    Draw the grid and player
    """
    window.clear()
    quadrados_batch.draw()
    menu(window)
    label_batch.draw()
    player.draw()

pyglet.app.run()
