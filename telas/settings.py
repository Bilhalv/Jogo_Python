import pyglet
from .Screen import Screen
from pyglet.window import mouse
import global_
from dificulty import *

# Create a screen
screen = Screen("Configurações")
batch = pyglet.graphics.Batch()

# Create a select box
bg = pyglet.shapes.Rectangle(0, screen.window.height//2 - 25//2, screen.window.width, 25, color=(0, 0, 255, 255), batch=batch)
knot = pyglet.shapes.Circle(screen.window.width//2, screen.window.height//2, 25, color=(255, 255, 255, 255), batch=batch)
label = pyglet.text.Label("Médio", y=screen.window.height//3, batch=batch, align="center", width=screen.window.width, color=(255, 255, 0, 255))
confirmar = pyglet.text.Label("Pressione enter para aceitar", y=50, batch=batch, align="center", width=screen.window.width, color=(255, 255, 0, 255))
dificuldade = 

def move_knot(x, screen):
    knot.x = x

def change_label(x:int, screen):
    easy = screen.window.width//4
    medium = screen.window.width - screen.window.width//4
    if x <= easy:
        label.text = "Fácil"
        label.color = (0, 255, 0, 255)
    elif x <= medium:
        label.text = "Médio"
        label.color = (255, 255, 0, 255)
    elif x > medium:
        label.text = "Difícil"
        label.color = (255, 0, 0, 255)

screen.draw(batch)

def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        global_.DIFICULDADE_ATUAL = label
        screen.window.close()

def runSettings():
    screen.start()