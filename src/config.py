# Maze and screen size configuration
SQUARE_SIZE = 40 # Size of each square in pixels
PADDING = 1 # Spacing between squares in pixels
MAZE_SIZE = 10 # Number of squares on each side of the maze
SCREEN_SIZE = MAZE_SIZE * (SQUARE_SIZE + PADDING) # Size of the window

# Colors configuration
DEFAULT_COLOR = (255, 255, 255, 100) # Default color for the squares
SECUNDARY_COLOR = (255, 255, 255, 200) # Color for the 3x3 grid
EXIT_COLOR = (255, 0, 0, 255) # Color for the exit square

# Other configuration
RANDOM_CHOICE = 2 # Used in the random.choice function for a more random behavior
TITLE = "Mage Maze" # Title of the game window
