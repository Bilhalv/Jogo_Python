import pyglet
import global_
from pyglet.window import mouse
from src.dificulty import *

# Create a window
window = pyglet.window.Window(400, 200, "Configurações")
batch = pyglet.graphics.Batch()
isClicking = [False, 0, 0]

# Create a select box
bg = pyglet.shapes.Rectangle(0, window.height//2-25//2, 400, 25, color=(0, 0, 255, 255), batch=batch)
knot = pyglet.shapes.Circle(200, 100, 25, color=(255, 255, 255, 255), batch=batch)
label = pyglet.text.Label("Médio", y=150, batch=batch, align="center", width=400, color=(255, 255, 0, 255))
confirmar = pyglet.text.Label("Pressione enter para aceitar", y=50, batch=batch, align="center", width=400, color=(255, 255, 0, 255))

def move_knot(x):
    knot.x = x

def change_label(x:int):
    easy = window.width//4
    medium = window.width//2
    hard = window.width*3//4
    if x <= easy:
        label.text = "Fácil"
        label.color = (0, 255, 0, 255)
        global_.DIFICULDADE_ATUAL = EASY
    elif x <= medium:
        label.text = "Médio"
        label.color = (255, 255, 0, 255)
        global_.DIFICULDADE_ATUAL = MEDIUM
    elif x >= hard:
        label.text = "Difícil"
        label.color = (255, 0, 0, 255)
        global_.DIFICULDADE_ATUAL = HARD

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons and mouse.LEFT:
        move_knot(x)
        change_label(x)
    else:
        print("Click")

if __name__ == "__main__":
    pyglet.app.run()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        window.close()
        from index import run_index
        run_index()

def runSettings():
    pyglet.app.run()