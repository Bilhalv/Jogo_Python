import pyglet
from src.config import *
from src.grid import criar_grid
from src.build_maze import build_maze
from src.player import build_player, move_player, show_3x3

window = pyglet.window.Window(SCREEN_SIZE, SCREEN_SIZE, "Hello, World!")

quadrados_batch, quadrados = criar_grid(SCREEN_SIZE, PADDING, SQUARE_SIZE)
entrada = [0, SCREEN_SIZE//(SQUARE_SIZE+PADDING)-1]
saida = [SCREEN_SIZE//(SQUARE_SIZE+PADDING)-1, 0]
andaveis = []

player_coord = [entrada[0]*(SQUARE_SIZE+PADDING)+(SQUARE_SIZE)/2, entrada[1]*(SQUARE_SIZE+PADDING)+(SQUARE_SIZE)/2]

build_maze(andaveis, entrada, saida, quadrados)
player = build_player(SQUARE_SIZE//4, player_coord)

show_3x3(entrada[0], entrada[1], andaveis, quadrados, entrada, saida)

@window.event
def on_key_press(symbol, modifiers):
    move_player(player=player, andaveis=andaveis, quadrados=quadrados, entrada=entrada, saida=saida, key=symbol, sqr=SQUARE_SIZE+PADDING)

@window.event
def on_draw():
    window.clear()
    quadrados_batch.draw()
    player.draw()

pyglet.app.run()