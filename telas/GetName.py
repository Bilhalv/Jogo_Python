import pyglet
import global_

# Create a window
window = pyglet.window.Window(400, 200, "Insira seu nome")

# Create a text input box
input_box = pyglet.text.Label(
    "",
    font_size=20,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x='center',
    anchor_y='center',
    multiline=False,
    width=200,
    color=(255, 255, 255, 255)
)

@window.event
def on_draw():
    window.clear()
    # Draw text
    label = pyglet.text.Label(
        "Insira seu nome:",
        font_size=20,
        x=window.width // 2,
        y=window.height // 2 + 30,
        anchor_x='center',
        anchor_y='center',
        color=(255, 255, 255, 255)
    )
    input_box.draw()
    label.draw()

@window.event
def on_text(text):
    if text.isalpha() and len(input_box.text) < 3:
        input_box.text += text.upper()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.BACKSPACE:
        input_box.text = input_box.text[:-1]
    elif symbol == pyglet.window.key.ENTER and len(input_box.text) == 3:
        from telas.game import run_game
        global_.NAME = str(input_box.text)
        window.close()
        run_game()

if __name__ == "__main__":
    pyglet.app.run()

def runGetName():
    pyglet.app.run()