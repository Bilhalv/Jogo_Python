import pyglet

from .Screen import Screen
from pyglet.window import mouse
import global_
from src.dificulty import *
import global_

def Run_Settings(settings):
    batch = pyglet.graphics.Batch()

    # Dificulty dict
    dificuldades = {
        EASY: [settings.window.width//4, "Fácil"],
        MEDIUM: [settings.window.width//2, "Médio"],
        HARD: [settings.window.width, "Difícil"]
    }

    # Create a select box
    DIF_TEMP = global_.DIFICULDADE_ATUAL
    bg = pyglet.shapes.Rectangle(0, settings.window.height//2 - 25//2, settings.window.width, 25, color=(0, 0, 255, 255), batch=batch)
    knot = pyglet.shapes.Circle(dificuldades[global_.DIFICULDADE_ATUAL][0], settings.window.height//2, 25, color=(255, 255, 255, 255), batch=batch)
    label = pyglet.text.Label(dificuldades[global_.DIFICULDADE_ATUAL][1], y=settings.window.height//3, batch=batch, align="center", width=settings.window.width, color=(255, 255, 0, 255))
    confirmar = pyglet.text.Label("Pressione enter para aceitar", y=50, batch=batch, align="center", width=settings.window.width, color=(255, 255, 0, 255))

    def move_knot(x, screen):
        knot.x = x
        @screen.window.event
        def on_draw():
            screen.clear()
            bg.draw()
            confirmar.draw()
            batch.draw()
            change_label(x, screen)

    def change_label(x:int, screen):
        global DIF_TEMP
        if x <= screen.window.width//4:
            label.text = "Fácil"
            label.color = (0, 255, 0, 255)
            DIF_TEMP = EASY
        elif x <= screen.window.width - screen.window.width//4:
            label.text = "Médio"
            label.color = (255, 255, 0, 255)
            DIF_TEMP = MEDIUM
        elif x > screen.window.width - screen.window.width//4:
            label.text = "Difícil"
            label.color = (255, 0, 0, 255)
            DIF_TEMP = HARD

    @settings.window.event
    def on_draw():
        settings.clear()
        settings.clear_listeners()
        batch.draw()

    @settings.window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        tolerancia = 100
        if buttons == mouse.LEFT and y < settings.window.height//2+tolerancia and y > settings.window.height//2-tolerancia:
            move_knot(x, settings)

    @settings.window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.ENTER:
            global DIF_TEMP
            import global_
            global_.DIFICULDADE_ATUAL = DIF_TEMP
            from .menu import Run_Menu
            Run_Menu(settings)