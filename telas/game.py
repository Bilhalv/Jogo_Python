import pyglet
from src.HUD.index import *
from src.config import *
from src.grid import Grid
from src.player import *
from telas.Screen import Screen

def run_Game(window:Screen):
    """
    Grid of squares
    """
    grid = Grid(window.window, SCREEN_SIZE, PADDING, SQUARE_SIZE)
    grid.build_maze()

    def winning():
        window.clear_listeners()
        grid._show_all()
        player.player.visible = False
        def add_highscore():
            highscore = open("highscore.txt", "a")
            highscore.write(f"{global_.NAME}: {global_.PASSOS//(global_.DIFICULDADE_ATUAL//2)}\n")
            highscore.close()
        @window.window.event
        def on_draw():
            pyglet.shapes.Rectangle(0, 0, window.window.width, window.window.height, color=(0, 0, 0, 50)).draw()
            pyglet.text.Label(
                text=f"Parabéns {global_.NAME}, você venceu com {global_.PASSOS//(global_.DIFICULDADE_ATUAL//2)} pontos!",
                color=(255, 255, 255, 255),
                font_size=50,
                y=window.window.height // 2,
                align="center",
                width=window.window.width
            ).draw()
        
        @window.window.event
        def on_key_press(symbol, modifiers):
            if symbol == pyglet.window.key.ESCAPE:
                window.window.close()
            elif symbol == pyglet.window.key.ENTER:
                from .menu import Run_Menu
                Run_Menu(window)
        add_highscore()

    """
    Player
    """
    player = Player(grid)

    """
    Draw the grid and player
    """
    @window.window.event
    def on_draw():
        window.clear()
        grid.batch.draw()
        grid.label_batch.draw()
        player.draw()
    
    @window.window.event
    def on_key_press(symbol, modifiers):
        isWin = False
        if symbol == pyglet.window.key.ESCAPE:
            window.window.close()
        elif symbol == pyglet.window.key.H:
            grid._show_all()
        elif symbol == pyglet.window.key.R:
            grid.build_maze()
        else:
            isWin = player.move(symbol)
        
        if isWin:
            winning()