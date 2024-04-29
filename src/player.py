import pyglet
from .config import *
from .grid import Grid

class Player:
    def __init__(self, grid:Grid):
        """
        Player object

        Parameters:
            grid (Grid): grid object
            entrance (list): coordinates of the entrance
            exit (list): coordinates of the exit
        """
        self.grid = grid
        self.step = grid.square_size
        self.pos_grid = [grid.entrance[0], grid.entrance[1]]
        self.player = pyglet.shapes.Circle(
            x=grid.squares_grid[grid.entrance[0]][grid.entrance[1]].x + grid.square_size // 2,
            y=grid.squares_grid[grid.entrance[0]][grid.entrance[1]].y + grid.square_size // 2,
            radius=grid.square_size // 3,
            color=(100, 0, 100, 255)
        )

    def draw(self):
        """
        Draw the player
        """
        self.player.draw()

    def remove(self):
        """
        Remove the player
        """
        self.player.delete()

    def update(self):
        """
        Update the player
        """
        self.remove()
        self.draw()

    def move(self, key):
        """
        Move the player based on keyboard input
    
        Parameters:
            key (int): the key that was pressed
        """
        isWin = False
        
        dx = {pyglet.window.key.LEFT: -self.step, pyglet.window.key.A: 0,
              pyglet.window.key.RIGHT: self.step, pyglet.window.key.D: 0}.get(key, 0)
        
        dy = {pyglet.window.key.UP:    self.step, pyglet.window.key.W: self.step,
              pyglet.window.key.DOWN:   -self.step, pyglet.window.key.S:   -self.step}.get(key, 0)
        
        new_pos = self.player.x + dx, self.player.y + dy
        new_grid = self.grid.find_on_grid(new_pos)
        if key not in {pyglet.window.key.UP, pyglet.window.key.DOWN, pyglet.window.key.LEFT, pyglet.window.key.RIGHT}:
            print("Invalid key")
            return
    
        if new_grid == self.grid.exit:
            isWin = True
            print("ganhou")
        
        if new_grid in self.grid._get_walkable_coords():
            self.player.x = self.grid.squares_grid[new_grid[0]][new_grid[1]].x + self.grid.square_size // 2
            self.player.y = self.grid.squares_grid[new_grid[0]][new_grid[1]].y + self.grid.square_size // 2
            self.grid._show_3x3(new_grid)
            global_.PASSOS += 1
        else:
            print("parede")
        
        return isWin