# index.py
# Import the Screen class from Screen.py
from .Screen import Screen
from utils import Button
import pyglet

def Run_Menu(menu:Screen):
    buttons_batch = pyglet.graphics.Batch()

    def start_button():
        print("Start")
        menu._clear_all
        from .GetName import Run_GetName
        Run_GetName(menu)

    def settings_button():
        print("Settings")
        menu._clear_all
        from telas.settings import Run_Settings
        Run_Settings(menu)

    def highscores_button():
        print("Ranking")
        menu._clear_all
        from telas.highscore import Run_Highscore
        Run_Highscore(menu)

    # Modify the window-related operations to use the Screen instance
    @menu.window.event
    def on_mouse_press(x, y, _, __):
        for button in buttons:
            if button.check_click(x, y):
                button.perform_action()

    @menu.window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            menu.window.close()
        if symbol == pyglet.window.key.SPACE:
            start_button()
        if symbol == pyglet.window.key.H:
            highscores_button()

    @menu.window.event
    def on_draw():
        menu.clear()
        buttons_batch.draw()

    buttons_dict = {
        "Jogar": {
            "y": 0,
            "function": start_button
        },
        "Configurações": {
            "y": 0,
            "function": settings_button
        },
        "Ranking": {
            "y": 0,
            "function": highscores_button
        }
    }

    buttons = []
    padding = 5
    height = 100
    width = 300
    for i, button in enumerate(buttons_dict):
        buttons.append(Button(
            x=menu.window.width//2,
            y=menu.window.height*0.85 - (len(buttons_dict) + i) * (height + padding),
            text=button,
            batch=buttons_batch,
            function=buttons_dict[button]["function"],
            width=width,
            height=height
        ))

    # Start the event loop
    pyglet.app.run()
    