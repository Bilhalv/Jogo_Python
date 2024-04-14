import pyglet
from src.config import *
from src.grid import criar_grid
from src.build_maze import build_maze
from src.player import build_player, move_player, show_3x3

"""
Main window
"""
window = pyglet.window.Window(SCREEN_SIZE, SCREEN_SIZE, "Labirinto do mago!")

"""
Grid of squares
"""
quadrados_batch, quadrados = criar_grid(SCREEN_SIZE, PADDING, SQUARE_SIZE)

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
build_maze(andaveis, entrada, saida, quadrados)

# create player
player = build_player(SQUARE_SIZE//4, player_coord)

# show the starting positions
show_3x3(entrada[0], entrada[1], andaveis, quadrados, entrada, saida)
andaveis.append(entrada)
andaveis.append(saida)

@window.event
def on_key_press(symbol, modifiers):
    """
    Handle player movement
    """
    move_player(player=player, andaveis=andaveis, quadrados=quadrados, entrada=entrada, saida=saida, key=symbol, sqr=SQUARE_SIZE+PADDING)


@window.event
def on_draw():
    """
    Draw the grid and player
    """
    window.clear()
    quadrados_batch.draw()
    player.draw()

pyglet.app.run()
