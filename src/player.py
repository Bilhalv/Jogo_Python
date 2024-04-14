"""
This module contains functions for handling player movement.
"""
import pyglet

from .config import SECUNDARY_COLOR, SQUARE_SIZE
from .grid import update_matriz

def draw_alert(message, window):
    dialog = pyglet.text.Label(message,
                               font_name='Arial',
                               font_size=16,
                               x=window.width // 2, y=window.height // 2,
                               anchor_x='center', anchor_y='center')
    
    exit = pyglet.text.Label("Pressione espaço para sair",
                             font_name='Arial',
                             font_size=16,
                             x=window.width // 2, y=window.height // 2 - 30,
                             anchor_x='center', anchor_y='center')
    bg = pyglet.shapes.Rectangle(x=0, y=0, width=window.width, height=window.height, color=(0, 0, 0, 10))
    @window.event
    def on_draw():
        bg.draw()
        dialog.draw()
        exit.draw()
    
    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            window.close()


def build_player(size, coord):
    """
    Builds a player object.

    Parameters:
        size (int): radius of the player in pixels.
        coord (list): coordinates of the player's center.

    Returns:
        a pyglet.shapes.Circle object representing the player.
    """
    player = pyglet.shapes.Circle(
        x=coord[0],
        y=coord[1],
        radius=size,
        color=(100, 0, 100, 255)
    )
    return player


def show_3x3(x, y, andaveis, quadrados, entrada, saida):
    """
    Highlights the 3x3 grid around the player.

    Parameters:
        x (int): x-coordinate of the player.
        y (int): y-coordinate of the player.
        andaveis (list): list of walkable coordinates.
        quadrados (list): list of squares Sprites.
        entrada (list): coordinates of the entrance.
        saida (list): coordinates of the exit.
    """
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


def move_player(andaveis, sqr, player, quadrados, entrada, saida, key, window):
    """
    Moves the player based on keyboard input.

    Parameters:
        andaveis (list): list of walkable coordinates.
        sqr (int): size of each square in pixels.
        player (pyglet.shapes.Circle): player object.
        quadrados (list): list of squares Sprites.
        entrada (list): coordinates of the entrance.
        saida (list): coordinates of the exit.
        key (int): the key that was pressed.
    """
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

    if new_grid == saida:
        draw_alert("Parabéns, você encontrou o tesouro!", window)
        return
    
    if new_grid in andaveis:
        player.x = new_pos[0]
        player.y = new_pos[1]
        show_3x3(player.x//sqr, player.y//sqr, andaveis, quadrados, entrada, saida)

