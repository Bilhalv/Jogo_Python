#here will be the HUD
import math
import pyglet
from pyglet.shapes import Rectangle
from .ref import HUD
from .config import HUD_SIZE

width = 400

window = pyglet.window.Window(
    width,
    HUD_SIZE,
    "HUD"
)

buttons = []
labels =[
    "Start",
    "Exit",
    "Start",
    "Exit",
]

button_width = 90
button_height = HUD_SIZE-10
button_padding = 5
button_spacing = 10

for i in range(math.ceil((width - button_spacing) / (button_width + button_spacing))):
    x = i * (button_width + button_spacing) + button_padding
    buttonBG = Rectangle(
        x=x, y=button_padding,
        width=button_width, height=button_height,
        color=(255, 255, 255, 255),
        batch=HUD
    )
    buttonFRONT = Rectangle(
        x=x + 4, y=button_padding + 4,
        width=button_width - 8, height=button_height - 8,
        color=(100, 0, 100, 255),
        batch=HUD
    )
    label = pyglet.text.Label(
        text=labels[i],
        x=x+4,
        y=math.floor(HUD_SIZE/2)-4,
        width=button_width - 8, height=button_height - 8,
        align='center',
        batch=HUD,
        color=(255, 255, 255, 150)
    )

    button = [buttonBG, buttonFRONT, label]
    buttons.append(button)

@window.event
def on_mouse_motion(x, y, dx, dy):
    for button in buttons:
        if button[0].x <= x <= button[0].x + button_width and button[0].y <= y <= button[0].y + button_height:
            button[1].color = (100, 0, 100, 100)
        else:
            button[1].color = (100, 0, 100, 255)

@window.event
def on_mouse_press(x, y, button, modifiers):
    for button in buttons:
        if button[0].x <= x <= button[0].x + button_width and button[0].y <= y <= button[0].y + button_height:
            if button[1].color == (255, 255, 255, 255):
                button[1].color = (100, 0, 100, 255)
            else:
                button[1].color = (255, 255, 255, 255)

@window.event
def on_draw():
    window.clear()
    HUD.draw()

def open_hud():
    pyglet.app.run()