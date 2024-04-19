"""
This module contains functions for handling player movement.
"""
import pyglet

from .config import *
from .grid import set_label, update_matriz
import global_
from .highscore import add_highscore

def draw_alert(message, window):
    dialog = pyglet.text.Label(message,
                               font_name='Arial',
                               font_size=16,
                               multiline=True,
                               width=window.width // 2,
                               x=window.width // 4, y=window.height // 2,
                               align='center')
    bg = pyglet.shapes.Rectangle(x=0, y=0, width=window.width, height=window.height, color=(0, 0, 0, 5))
    @window.event
    def on_draw():
        bg.draw()
        dialog.draw()
    
    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            window.close()
            from index import run_index
            run_index()
            run_index()


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


def show_3x3(x, y, andaveis, quadrados, entrada, saida, labels):
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
    up: list = [x, y+1]
    down: list = [x, y-1]
    left: list = [x-1, y]
    right: list = [x+1, y]
    
    def find_color(coord):
        if coord != entrada and coord != saida:
            color = WALL_COLOR
            if coord in andaveis:
                color = FLOOR_COLOR
            set_label(coord[0], coord[1], labels, "")
            return color
    
    up_color = find_color(up)
    down_color = find_color(down)
    left_color = find_color(left)
    right_color = find_color(right)
    
    for i in [[up, up_color], [down, down_color], [left, left_color], [right, right_color]]:
        update_matriz(i[0][0], i[0][1], i[1], quadrados)


def move_player(andaveis, sqr, player, quadrados, entrada, saida, key, window, labels):
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
        draw_alert(F"Parabéns, {global_.NAME}, você encontrou o tesouro em {global_.PASSOS} passos!", window)
        add_highscore(str(global_.PASSOS)+" - "+str(global_.NAME))
        return
    
    if new_grid in andaveis:
        player.x = new_pos[0]
        player.y = new_pos[1]
        show_3x3(player.x//sqr, player.y//sqr, andaveis, quadrados, entrada, saida, labels)
        global_.PASSOS += 1

