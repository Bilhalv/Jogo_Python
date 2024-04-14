from pyglet import shapes
import pyglet

from .config import SECUNDARY_COLOR, SQUARE_SIZE
from .grid import update_matriz

def build_player(size, coord):
    player = shapes.Circle(
        x=coord[0],
        y=coord[1],
        radius=size,
        color=(100, 0, 100, 255)
    )
    return player 

def show_3x3(x, y, andaveis, quadrados, entrada, saida):
    x, y = int(x), int(y)
    up = [x, y+1]
    down = [x, y-1]
    left = [x-1, y]
    right = [x+1, y]
    if up in andaveis and up != entrada and up != saida:
        update_matriz(up[0], up[1], SECUNDARY_COLOR, quadrados)
    if down in andaveis and down != entrada and down != saida:
        update_matriz(down[0], down[1], SECUNDARY_COLOR, quadrados)
    if left in andaveis and left != entrada and left != saida:
        update_matriz(left[0], left[1], SECUNDARY_COLOR, quadrados)
    if right in andaveis and right != entrada and right != saida:
        update_matriz(right[0], right[1], SECUNDARY_COLOR, quadrados)

def move_player(andaveis, sqr, player, quadrados, entrada, saida, key):
    if key == pyglet.window.key.UP or key == pyglet.window.key.W:
        new_pos = [player.x, player.y+sqr]
        new_grid = [int(player.x//sqr), int((player.y + sqr)//sqr)]
    elif key == pyglet.window.key.DOWN or key == pyglet.window.key.S:
        new_pos = [player.x, player.y-sqr]
        new_grid = [int(player.x//sqr), int((player.y - sqr)//sqr)]
    elif key == pyglet.window.key.LEFT or key == pyglet.window.key.A:
        new_pos = [player.x-sqr, player.y]
        new_grid = [int((player.x - sqr)//sqr), int(player.y//sqr)]
    elif key == pyglet.window.key.RIGHT or key == pyglet.window.key.D:
        new_pos = [player.x+sqr, player.y]
        new_grid = [int((player.x + sqr)//sqr), int(player.y//sqr)]
    else:
        return

    if new_grid in andaveis:
        player.x = new_pos[0]
        player.y = new_pos[1]
        show_3x3(player.x//sqr, player.y//sqr, andaveis, quadrados, entrada, saida)
