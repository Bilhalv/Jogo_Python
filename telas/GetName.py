import select
import pyglet
import global_
from .Screen import Screen
from pyglet import shapes

def Run_GetName(window:Screen):
    # Create a list to store the selected letters
    selected_letters = [
        {"key": "A", "x": window.window.width // 2 - 20},
        {"key": "B", "x": window.window.width // 2 - 5},
        {"key": "C", "x": window.window.width // 2 + 10}
    ]
    
    # Create a text input box
    input_box = pyglet.text.Label(
        ''.join([letter["key"] for letter in selected_letters]),
        font_size=20,
        x=window.window.width // 2,
        y=window.window.height // 2,
        anchor_x='center',
        anchor_y='center',
        multiline=False,
        width=200,
        color=(255, 255, 255, 255)
    )
    
    arrow = shapes.Triangle(
        x=window.window.width // 2 - 5,
        x2=window.window.width // 2 + 5,
        x3=window.window.width // 2,
        
        y=window.window.height // 2 - 25,
        y2=window.window.height // 2 - 25,
        y3=window.window.height // 2 -20,
        
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
        arrow.draw()
    
    @window.window.event
    def on_text(text):
        idx = 0
        for i, letter in enumerate(selected_letters):
                if letter["x"] == arrow.x:
                    idx = i
                    break
        selected_letters[idx]["key"] = text.upper()
        input_box.text = ''.join([letter["key"] for letter in selected_letters])
        input_box.draw()

    @window.window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.LEFT or symbol == pyglet.window.key.RIGHT:
            idx = 0
            for i, letter in enumerate(selected_letters):
                if letter["x"] == arrow.x:
                    idx = i
                    break
            if symbol == pyglet.window.key.LEFT and idx > 0:
                idx -= 1
            elif symbol == pyglet.window.key.RIGHT and idx < 2:
                idx += 1
            arrow.x = selected_letters[idx]["x"]
            arrow.draw()
        elif symbol == pyglet.window.key.ENTER:
            global_.NAME = ''.join([letter["key"] for letter in selected_letters])
            from telas.game import run_Game
            run_Game(window)
