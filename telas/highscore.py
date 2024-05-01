from tkinter import font
import pyglet
from pyglet.window import key
from src.highscore import get_highscore
from telas.Screen import Screen


def Run_Highscore(highscore:Screen):
    batch = pyglet.graphics.Batch()

    # txt com os highscores
    highscores = []
    for i, line in enumerate(get_highscore()):
        name, score = line
        high = [
            pyglet.text.Label(
                name,
                align="left",
                x=highscore.window.width // 4,
                y=highscore.window.height // 2 - 50 * i + 125,
                anchor_y="center",
                anchor_x="center",
                batch=batch,
                width=highscore.window.width//2,
                color=(255, 255, 0, 255),
                font_size=50,
                font_name="Consolas"
            ),
            pyglet.text.Label(
                str(score),
                align="right",
                x=highscore.window.width // 4,
                y=highscore.window.height // 2 - 50 * i + 125,
                anchor_y="center",
                anchor_x="center",
                batch=batch,
                width=highscore.window.width//2,
                color=(255, 255, 0, 255),
                font_size=50,
                font_name="Consolas"
            )
        ]
        highscores.append(high)

    # Create a select box
    confirmar = pyglet.text.Label("Pressione enter para voltar", y=50, batch=batch, align="center", width=highscore.window.width, color=(255, 255, 0, 255))

    @highscore.window.event
    def on_draw():
        highscore.clear()
        highscore.clear_listeners()
        confirmar.draw()
        for high in highscores:
            high[0].draw()
            high[1].draw()
        batch.draw()

    @highscore.window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.ENTER:
            highscore.clear()
            from .menu import Run_Menu
            Run_Menu(highscore)