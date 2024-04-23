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
        if symbol == pyglet.window.key.ESCAPE:
            window.window.close()
        else:
            player.move(symbol)