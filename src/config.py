# Size configuration
SQUARE_SIZE = 60 # Size of each square in pixels
PADDING = 1 # Spacing between squares in pixels
MAZE_SIZE = 5 # Number of squares on each side of the maze
SCREEN_SIZE = MAZE_SIZE * (SQUARE_SIZE + PADDING) # Size of the window
MENU_SIZE = 50
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

# Colors configuration
EXIT_COLOR = (0, 150, 0, 255) # Color for the exit square
BG_COLOR = (0, 0, 0, 255) # Color for the background
UNDISCOVERED_COLOR = (255, 255, 255, 100) # Color for the undiscovered squares
ENTRANCE_COLOR = (150, 0, 0, 255) # Color for the entrance square
FLOOR_COLOR = (255, 255, 255, 200) # Color for the floor
WALL_COLOR = (0, 0, 0, 255) # Color for the wall
BG_MENU_COLOR = (0, 0, 0, 255)
BG_BUTTON_COLOR = (255, 255, 255, 255)
BUTTON_LABEL_COLOR = (0, 0, 0, 255)

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
NAME = ""
PASSOS = 0