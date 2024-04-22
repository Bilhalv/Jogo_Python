import pyglet

from telas.Screen import Screen

# Create the main window
window = Screen("Labirinto do mago!")

# Start the menu
from telas.menu import Run_Menu
Run_Menu(window)