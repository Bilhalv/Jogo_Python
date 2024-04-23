"""
Creates a grid of squares to be used as a playable space.
"""
import pyglet
from pyglet import shapes
from .config import *
import random

class Grid:
    def __init__(self, window:pyglet.window.Window, side_screen:int, space:int, square_size:int):
        self.window = window
        self.side_screen = side_screen
        self.space = space
        self.square_size = square_size
        self.batch = pyglet.graphics.Batch()
        self.label_batch = pyglet.graphics.Batch()
        self.squares_grid:list[list[pyglet.shapes.Rectangle]] = self._create_grid()
        self.labels_grid = self._create_labels()
        self.walkable:list[tuple[int, int]] = []
        self.entrance:tuple[int, int] = (0, len(self.squares_grid) - 1)
        self.exit:tuple[int, int] = (len(self.squares_grid) - 1, 0)

    def build_maze(self) -> None:
        """Recursive backtracking algorithm to build a maze"""
        def num_walkable_neighbors(x: int, y: int) -> int:
            """Count number of walkable neighbors"""
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            return sum(
                1 for n_x, n_y in neighbors
                if 0 <= n_x < len(self.squares_grid) and
                0 <= n_y < len(self.squares_grid[0]) and
                self._get_square([n_x, n_y]).color == FLOOR_COLOR)

        current:tuple[int, int] = self.entrance

        while True:
            # Check if we've reached the exit
            if current == self.exit:
                break

            # Generate all possible moves
            options = [
                c for c in [(current[0], current[1] + 1),
                            (current[0], current[1] - 1),
                            (current[0] + 1, current[1]),
                            (current[0] - 1, current[1])]
                if 0 <= c[0] < len(self.squares_grid) and
                0 <= c[1] < len(self.squares_grid[0]) and
                num_walkable_neighbors(c[0], c[1]) <= 3
            ]

            # If we have no options, backtrack
            if not options:
                if not self.walkable:
                    current = self.entrance
                else:
                    current = random.choice(self._get_walkable_coords())

            # If we have options, choose one and update the list of walkable coords
            else:
                current = random.choice(options)
                temp:list[tuple[int, int]] = self._get_walkable_coords()
                temp.append(current)
                self._set_walkable_coords(temp)
        self._show_3x3(self.entrance)

    def _get_square(self, coord: list[int]) -> pyglet.shapes.Rectangle:
        if 0 <= coord[0] < len(self.squares_grid) and 0 <= coord[1] < len(self.squares_grid[0]):
            return self.squares_grid[coord[0]][coord[1]]
        else:
            return self.squares_grid[0][0]

    def _get_walkable(self, coord:list[int]):
        coords = self._get_walkable_coords()
        return coords[coord[0]][coord[1]] == True
    
    def _get_walkable_coords(self):
        return self.walkable
    
    def _set_walkable_coords(self, coords:list[tuple[int, int]]):
        self.walkable = coords

    def _create_grid(self):
        telaX = self.window.width - self.side_screen
        telaY = self.window.height - self.side_screen
        squares_grid = []
        for i in range(self.side_screen // (self.space + self.square_size)):
            squares_grid.append([])
            for j in range(self.side_screen // (self.space + self.square_size)):
                x = i * (self.space + self.square_size)
                y = j * (self.space + self.square_size)
                square = shapes.Rectangle(
                    x=x+telaX//2,
                    y=y+telaY//2,
                    width=self.square_size,
                    height=self.square_size,
                    color=UNDISCOVERED_COLOR,
                    batch=self.batch
                )
                squares_grid[i].append(square)
        return squares_grid

    def _create_labels(self):
        labels_grid = []
        for row in self.squares_grid:
            labels_grid.append([])
            for square in row:
                labels_grid[-1].append(self._build_label([square.x, square.y]))
        return labels_grid

    def _build_label(self, coord:list[int]):
        label = pyglet.text.Label(
            text=f"?",
            x=coord[0],
            y=coord[1] + self.square_size // 2,
            batch=self.label_batch,
            color=(255, 255, 255, 255),
            width=self.square_size,
            height=self.square_size,
            font_size=self.square_size//3,
            align="center"
        )
        return label

    def find_on_grid(self, coord:list[int]):
        for i, row in enumerate(self.squares_grid):
            for j, square in enumerate(row):
                if square.x <= coord[0] <= square.x + square.width and \
                        square.y <= coord[1] <= square.y + square.height:
                    return i, j
        return None, None

    def update_matriz(self, coord:list[int], color):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= len(self.squares_grid) or coord[1] >= len(self.squares_grid[0]):
            return
        if color == None:
            return
        self.squares_grid[coord[0]][coord[1]].color = color

    def set_label(self, coord:list[int], text):
        if 0 <= coord[0] < len(self.labels_grid) and 0 <= coord[1] < len(self.labels_grid):
            self.labels_grid[coord[0]][coord[1]].text = text
    
    def _show_3x3(self, coord:tuple[int, int]):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= coord[0] + i < len(self.squares_grid) and 0 <= coord[1] + j < len(self.squares_grid):
                    square = self.squares_grid[coord[0] + i][coord[1] + j]
                    if (coord[0]+i, coord[1]+j) in self.walkable:
                        square.color = FLOOR_COLOR
                    elif (coord[0]+i, coord[1]+j) == self.entrance:
                        square.color = ENTRANCE_COLOR
                    elif (coord[0]+i, coord[1]+j) == self.exit:
                        square.color = EXIT_COLOR
                    else:
                        square.color = WALL_COLOR
                    self.labels_grid[coord[0] + i][coord[1] + j].visible = False