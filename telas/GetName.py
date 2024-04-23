import pyglet
import global_
from .Screen import Screen

def Run_GetName(window:Screen):

    # Create a text input box
    input_box = pyglet.text.Label(
        "AAA",
        font_size=20,
        x=window.window.width // 2,
        y=window.window.height // 2,
        anchor_x='center',
        anchor_y='center',
        multiline=False,
        width=200,
        color=(255, 255, 255, 255)
    )

    @window.window.event
    def on_draw():
        window.window.clear()
        # Draw text
        label = pyglet.text.Label(
            "Insira seu nome:",
            font_size=20,
            x=window.window.width // 2,
            y=window.window.height // 2 + 30,
            anchor_x='center',
            anchor_y='center',
            color=(255, 255, 255, 255)
        )
        input_box.draw()
        label.draw()

    @window.window.event
    def on_text(text):
        if text.isalpha() and len(input_box.text) < 3:
            input_box.text += text.upper()

    @window.window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.BACKSPACE:
            input_box.text = input_box.text[:-1]
        elif symbol == pyglet.window.key.ENTER and len(input_box.text) == 3:
            from telas.game import run_Game
            global_.NAME = str(input_box.text)
            run_Game(window)