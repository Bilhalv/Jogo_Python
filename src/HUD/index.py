from pyglet import shapes
import pyglet
from ..config import *

SCREEN_SIZE = global_.DIFICULDADE_ATUAL * (SQUARE_SIZE + PADDING)
START_COORD = [
    MENU_SIZE//10,
    SCREEN_SIZE+MENU_SIZE//4,
]
START_SIZE = [
    SCREEN_SIZE//2 - (MENU_SIZE//10)*2,
    MENU_SIZE//2
]
RESTART_COORD = [
    SCREEN_SIZE//2,
    SCREEN_SIZE+MENU_SIZE//4,
]
RESTART_SIZE = [
    SCREEN_SIZE//2 - (MENU_SIZE//10)*2,
    MENU_SIZE//2
]

def create_button_w_text(x, y, text, batch, color, text_color, width, height):
    bg = shapes.Rectangle(
        x,
        y,
        width,
        height,
        color,
        batch
    )
    label = pyglet.text.Label(
        text,
        x=x,
        y=y+height//4,
        batch=batch,
        color=text_color,
        align="center",
        width=width,
        height=height
    )
    return bg, label

def menu(window):
    """
    Builds the main menu.
    """
    menu = pyglet.graphics.Batch()
    bg = shapes.Rectangle(
        x=0,
        y=SCREEN_SIZE,
        width=SCREEN_SIZE,
        height=MENU_SIZE,
        color=BG_MENU_COLOR,
        batch=menu
    )
    
    start_bg, start_label = create_button_w_text(
        x=START_COORD[0],
        y=START_COORD[1],
        text="Return",
        batch=menu,
        color=BG_BUTTON_COLOR,
        text_color=BUTTON_LABEL_COLOR,
        width=START_SIZE[0],
        height=START_SIZE[1]
    )
    
    restart_bg, restart_label = create_button_w_text(
        x=RESTART_COORD[0],
        y=RESTART_COORD[1],
        text="Restart",
        batch=menu,
        color=BG_BUTTON_COLOR,
        text_color=BUTTON_LABEL_COLOR,
        width=RESTART_SIZE[0],
        height=RESTART_SIZE[1]
    )
    
    return menu.draw()


def isStart(x, y):
    if START_COORD[0] <= x <= START_COORD[0] + START_SIZE[0] and START_COORD[1] <= y <= START_COORD[1] + START_SIZE[1]:
        return True
    else:
        return False


def isRestart(x, y):
    if RESTART_COORD[0] <= x <= RESTART_COORD[0] + RESTART_SIZE[0] and RESTART_COORD[1] <= y <= RESTART_COORD[1] + RESTART_SIZE[1]:
        return True
    else:
        return False
