from pyglet import shapes
import pyglet
from ..config import SCREEN_SIZE, MENU_SIZE, START_COORD, START_SIZE, RESTART_COORD, RESTART_SIZE

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

def menu():
    """
    Builds the main menu.
    """
    menu = pyglet.graphics.Batch()
    bg = shapes.Rectangle(
        x=0,
        y=SCREEN_SIZE,
        width=SCREEN_SIZE,
        height=MENU_SIZE,
        color=(255, 0, 255),
        batch=menu
    )
    
    padding = MENU_SIZE//10
    
    start_bg, start_label = create_button_w_text(
        x=START_COORD[0],
        y=START_COORD[1],
        text="Return",
        batch=menu,
        color=(255, 255, 255, 255),
        text_color=(0, 0, 0, 255),
        width=START_SIZE[0],
        height=START_SIZE[1]
    )
    
    restart_bg, restart_label = create_button_w_text(
        x=RESTART_COORD[0],
        y=RESTART_COORD[1],
        text="Restart",
        batch=menu,
        color=(255, 255, 255, 255),
        text_color=(0, 0, 0, 255),
        width=RESTART_SIZE[0],
        height=RESTART_SIZE[1]
    )
    
    return menu.draw()