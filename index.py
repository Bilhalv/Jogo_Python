import pyglet
from src.config import *
from pyglet import shapes, text

window = pyglet.window.Window(SCREEN_SIZE, SCREEN_SIZE+MENU_SIZE, "Inicio!")

def boolStart(x, y):
    return True 

def boolHighscore(x, y):
    return True 

dict = {
    "Start": boolStart,
    "Highscore": boolHighscore
}

def make_button(xCoord:int,
                yCoord:int,
                text:str,
                batch,
                color: tuple,
                text_color: tuple,
                width:int,
                height:int,
                onClick,
                window  # Pass the window object as a parameter
                ):
    bg = shapes.Rectangle(
        x=xCoord,
        y=yCoord,
        width=width,
        height=height,
        color=color,
        batch=batch
    )
    label = pyglet.text.Label(
        text,
        x=xCoord,
        y=yCoord+height//4,
        batch=batch,
        color=text_color,
        font_size=20,
        width=width,
        height=height,
        align="center"
    )
    def bool (x, y):
        return bg.x < x < bg.x + bg.width and bg.y < y < bg.y + bg.height
    dict[text] = bool
    return bg, label

buttons = pyglet.graphics.Batch()

def start ():
    print("start")
    window.close()
    from game import run_game
    run_game()
    
def highscore ():
    print("highscore")
    @window.event
    def on_draw():
        window.clear()
        with open("highscore.txt", "r") as arq:
            linhas = arq.readlines()
            i = 0
            for linha in linhas:
                if "\n" in linha:
                    linha = linha[:-1]
                label = pyglet.text.Label(
                    linha,
                    x=(SCREEN_SIZE+MENU_SIZE)//4,
                    y=(SCREEN_SIZE+MENU_SIZE)//2 + 100 + i * 50,
                    batch=buttons,
                    color=(255, 255, 255, 255),
                    font_size=20
                )
                label.draw()
                i -= 1
    

start_button = make_button((SCREEN_SIZE+MENU_SIZE)//4, (SCREEN_SIZE+MENU_SIZE)//2, "Start", buttons, (0, 255, 0, 255), (255, 255, 255, 255), 200, 50, start, window)  # Pass window as an argument
highscore_button = make_button((SCREEN_SIZE+MENU_SIZE)//4, (SCREEN_SIZE+MENU_SIZE)//2 - 100, "Highscore", buttons, (0, 255, 0, 255), (255, 255, 255, 255), 200, 50, highscore, window)  # Pass window as an argument

@window.event
def on_mouse_press(x, y, button, modifiers):
    if dict["Start"](x, y):
        start()
    elif dict["Highscore"](x, y):
        highscore()

@window.event
def on_draw():
    window.clear()
    buttons.draw()

pyglet.app.run()

