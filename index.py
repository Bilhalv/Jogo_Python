import pyglet
from src.config import *
from pyglet import shapes 

START_HEIGHT = BUTTON_HEIGHT*4 + BUTTON_HEIGHT//2
START_WIDTH = BUTTON_WIDTH*2

# Window setup
window = pyglet.window.Window(START_WIDTH, START_HEIGHT, "Inicio")

# Button dictionary
button_dict = {}

# Functions for button actions
def start():
    print("Starting game...")
    window.close()
    from telas.GetName import runGetName
    runGetName()

def highscore():
    print("Viewing highscores...")
    show_highscores()

def show_highscores():
    @window.event
    def on_draw():
        window.clear()
        go_back_batch.draw()


def go_back():
    global is_high
    is_high = False
    @window.event
    def on_draw():
        window.clear()
        buttons_batch.draw()

# Button action functions
def create_bool(x, y, bgx, bgy):
    return bgx < x < bgx + BUTTON_WIDTH and bgy < y < bgy + BUTTON_HEIGHT

# Button creation function
def make_button(x_coord, y_coord, text, batch, color, text_color):
    bg = shapes.Rectangle(
        x=x_coord,
        y=y_coord,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        color=color,
        batch=batch
    )
    label = pyglet.text.Label(
        text,
        x=x_coord,
        y=y_coord + BUTTON_HEIGHT // 4,
        batch=batch,
        color=text_color,
        font_size=20,
        align="center",
        width=BUTTON_WIDTH,
    )
    button_dict[text] = lambda x, y: create_bool(x, y, bg.x, bg.y)
    return bg, label

# Initialize button batch
buttons_batch = pyglet.graphics.Batch()

go_back_batch = pyglet.graphics.Batch()

go_back_button_bg, go_back_button_label =   make_button(
    SCREEN_SIZE // 4,
    BUTTON_HEIGHT // 2,
    "Back",
    go_back_batch,
    (0, 255, 0, 255),
    (255, 255, 255, 255)
)

# Create buttons
start_button_bg, start_button_label = make_button(
    BUTTON_WIDTH//2,
    BUTTON_HEIGHT*2 + BUTTON_HEIGHT//2,
    "Start",
    buttons_batch,
    (0, 255, 0, 255),
    (255, 255, 255, 255)
)
highscore_button_bg, highscore_button_label = make_button(
    BUTTON_WIDTH//2,
    BUTTON_HEIGHT,
    "Highscore",
    buttons_batch,
    (0, 255, 0, 255),
    (255, 255, 255, 255)
)

high = []
with open("highscore.txt", "r") as file:
    highscore_lines = file.readlines()
    for idx, line in enumerate(highscore_lines):
        line = line.rstrip()
        if idx == 5:
            break
        label = pyglet.text.Label(
            line,
            x=START_WIDTH // 4,
            y=START_HEIGHT - (idx+1) * 25,
            color=(255, 255, 255, 255),
            font_size=15,
            batch=go_back_batch,
            align="center",
            width=START_WIDTH // 2
        )
        high.append(label)

# Event handlers
@window.event
def on_mouse_press(x, y, button, modifiers):
    global is_high
    dict = button_dict
    if dict["Start"](x, y) and not is_high:
        start()
    elif dict["Highscore"](x, y) and not is_high:
        is_high = True
        show_highscores()
    elif dict["Back"](x, y) and is_high:
        is_high = False
        go_back()

@window.event
def on_draw():
    window.clear()
    buttons_batch.draw()

# Application entry point
if __name__ == "__main__":
    is_high = False
    pyglet.app.run()