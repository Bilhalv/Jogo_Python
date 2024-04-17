import pyglet
from pyglet import shapes
from src.config import *
from src.highscore import get_highscore

START_HEIGHT = BUTTON_HEIGHT * 4 + BUTTON_HEIGHT // 2
START_WIDTH = BUTTON_WIDTH * 2
num_buttons = 3
margem = 2
margem_inicial =  ((BUTTON_HEIGHT + margem) * num_buttons)*2

class Button:
    def __init__(self, x, y, text, color, text_color, action, batch):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.text_color = text_color
        self.action = action
        self.batch = batch
        
        if (batch == buttons_batch):
            global num_buttons
            y = margem_inicial - ((BUTTON_HEIGHT + margem) * num_buttons)
            num_buttons -= 1

        # Calculate button size dynamically based on available space
        button_width = min(BUTTON_WIDTH, START_WIDTH - x)
        button_height = min(BUTTON_HEIGHT, START_HEIGHT - y)

        self.bg = shapes.Rectangle(
            x=x, y=y, width=button_width, height=button_height,
            color=color, batch=batch
        )
        self.label = pyglet.text.Label(
            text, x=x, y=y + button_height // 4, batch=batch,
            color=text_color, font_size=20, align="center", width=button_width
        )

    def check_click(self, x, y):
        return self.x < x < self.x + self.bg.width and self.y < y < self.y + self.bg.height

    def perform_action(self):
        self.action()

def start_game():
    print("Starting game...")
    window.close()
    from telas.GetName import runGetName
    runGetName()

def view_highscores():
    print("Viewing highscores...")
    show_highscores()

def show_highscores():
    global is_high
    is_high = True
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

# Initialize window and batches
window = pyglet.window.Window(START_WIDTH, START_HEIGHT, "Inicio")
buttons_batch = pyglet.graphics.Batch()
go_back_batch = pyglet.graphics.Batch()

# Create buttons
buttons = []
buttons.append(Button(
    BUTTON_WIDTH // 2, BUTTON_HEIGHT * 2 + BUTTON_HEIGHT // 2,
    "Start", (0, 255, 0, 255), (255, 255, 255, 255), start_game, buttons_batch
))
buttons.append(Button(
    BUTTON_WIDTH // 2, BUTTON_HEIGHT, "Highscore",
    (0, 255, 0, 255), (255, 255, 255, 255), view_highscores, buttons_batch
))
buttons.append(Button(
    BUTTON_WIDTH // 2, BUTTON_HEIGHT, "A",
    (0, 255, 0, 255), (255, 255, 255, 255), view_highscores, buttons_batch
))
buttons.append(Button(
    BUTTON_WIDTH // 2, BUTTON_HEIGHT // 2, "Back",
    (0, 255, 0, 255), (255, 255, 255, 255), go_back, go_back_batch
))

# Highscore display
highscore_lines = get_highscore()
highscore_labels = []
for idx, line in enumerate(highscore_lines):
    num_text, score_text = line.split(" - ")
    num_label = pyglet.text.Label(
        num_text, x=BUTTON_WIDTH // 2, y=START_HEIGHT - BUTTON_HEIGHT - idx * 20,
        batch=go_back_batch, color=(255, 255, 255, 255), font_size=12,
        width=BUTTON_WIDTH, align="right", font_name='Consolas'
    )
    score_label = pyglet.text.Label(
        str(idx+1)+"º "+score_text, x=BUTTON_WIDTH // 2, y=START_HEIGHT - BUTTON_HEIGHT - idx * 20,
        batch=go_back_batch, color=(255, 255, 255, 255), font_size=12,
        width=BUTTON_WIDTH, align="left", font_name='Consolas'
    )
    highscore_labels.append((num_label, score_label))

# Event handlers
@window.event
def on_mouse_press(x, y, button, modifiers):
    for button in buttons:
        if button.check_click(x, y):
            button.perform_action()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ESCAPE:
        window.close()
    if symbol == pyglet.window.key.SPACE:
        start_game()
    if symbol == pyglet.window.key.H:
        view_highscores()

@window.event
def on_draw():
    window.clear()
    buttons_batch.draw()
    go_back_batch.draw() if is_high else None

# Application entry point
if __name__ == "__main__":
    is_high = False
    pyglet.app.run()

def run_index():
    global is_high
    is_high = False
    pyglet.app.run()
