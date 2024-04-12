#here will be the HUD
import pyglet # type: ignore
from pyglet import shapes # type: ignore
from .ref import HUD
from .config import HUD_SIZE

width = 400

window = pyglet.window.Window(
    width,
    HUD_SIZE,
    "HUD"
)

buttons = [
    pyglet.shapes.Rectangle(0, 0, 50, 50, color=(255, 255, 255), batch=HUD),
    pyglet.shapes.Rectangle(50, 0, 50, 50, color=(255, 255, 255), batch=HUD),
    pyglet.shapes.Rectangle(100, 0, 50, 50, color=(255, 255, 255), batch=HUD),
    pyglet.shapes.Rectangle(150, 0, 50, 50, color=(255, 255, 255), batch=HUD),
    pyglet.shapes.Rectangle(200, 0, 50, 50, color=(255, 255, 255), batch=HUD),
    pyglet.shapes.Rectangle(250, 0, 50, 50, color=(255, 255, 255), batch=HUD),
    pyglet.shapes.Rectangle(300, 0, 50, 50, color=(255, 255, 255), batch=HUD),
    pyglet.shapes.Rectangle(350, 0, 50, 50, color=(255, 255, 255), batch=HUD),
]

@window.event
def on_draw():
    window.clear()
    HUD.draw()
    
    
def open_hud():
    pyglet.app.run()