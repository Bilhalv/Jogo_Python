# Size configuration
SQUARE_SIZE = 40 # Size of each square in pixels
PADDING = 1 # Spacing between squares in pixels
MAZE_SIZE = 10 # Number of squares on each side of the maze
SCREEN_SIZE = MAZE_SIZE * (SQUARE_SIZE + PADDING) # Size of the window
MENU_SIZE = 50

# Colors configuration
DEFAULT_COLOR = (255, 255, 255, 100) # Default color for the squares
SECUNDARY_COLOR = (255, 255, 255, 200) # Color for the 3x3 grid
EXIT_COLOR = (255, 0, 0, 255) # Color for the exit square

# Other configuration
RANDOM_CHOICE = 2 # Used in the random.choice function for a more random behavior
TITLE = "Mage Maze" # Title of the game window

# Button Coords
START_COORD = [
    MENU_SIZE//10,
    SCREEN_SIZE+MENU_SIZE//4,
]
START_SIZE = [
    SCREEN_SIZE//2 - (MENU_SIZE//10)*2,
    MENU_SIZE//2
]
RESTART_COORD = [
    SCREEN_SIZE//2,
    SCREEN_SIZE+MENU_SIZE//4,
]
RESTART_SIZE = [
    SCREEN_SIZE//2 - (MENU_SIZE//10)*2,
    MENU_SIZE//2
]