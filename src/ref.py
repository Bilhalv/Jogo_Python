from .config import MAZE_SIZE
import pyglet # type: ignore

matriz = []
exit = [0, MAZE_SIZE-1]
entrance = [MAZE_SIZE-1, 0]
isWalkable = [entrance]
HUD = pyglet.graphics.Batch()