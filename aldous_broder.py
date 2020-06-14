# A program which uses Aldous-Broder Algorithm to generate a maze

import random
from enum import Enum
import numpy as np
import cv2


class Directions(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Aldous_Broder:

    def __init__(self, height, width, path, displayMaze):

        print("Using OpenCV version: " + cv2.__version__)

        if width % 2 == 0:
            width += 1
        if height % 2 == 0:
            height += 1

        self.width = width
        self.height = height
        self.path = path
        self.displayMaze = displayMaze

    def createMaze(self):
        maze = np.ones((self.height, self.width), dtype=np.float)

        for i in range(self.height):
            for j in range(self.width):
                if i % 2 == 1 or j % 2 == 1:
                    maze[i, j] = 0
                if i == 0 or j == 0 or i == self.height - 1 or j == self.width - 1:
                    maze[i, j] = 0.5

        sx = random.choice(range(2, self.width - 2, 2))
        sy = random.choice(range(2, self.height - 2, 2))

        self.generator(sx, sy, maze)

        for i in range(self.height):
            for j in range(self.width):
                if not maze[i, j] == 0:
                    maze[i, j] = 1

        maze[1, 2] = 1
        maze[self.height - 2, self.width - 3] = 1

        if self.displayMaze:
            cv2.namedWindow('Maze', cv2.WINDOW_NORMAL)
            cv2.imshow('Maze', maze)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        maze = maze * 255.0
        cv2.imwrite(self.path, maze)

        return 0

    def generator(self, x, y, grid):
        grid[y, x] = 0.5

        v = ((self.height - 5)/2 + 1) * ((self.width - 5)/2 + 1)

        # while all cells have not been visited
        while v > 1:

            dir = random.randint(1, 4)

            if dir == Directions.UP.value:
                if grid[y - 2, x] == 1:
                    grid[y - 2, x] = 0.5
                    grid[y - 1, x] = 0.5
                    v -= 1
                if not y == 2:
                    y -= 2
            elif dir == Directions.DOWN.value:
                if grid[y + 2, x] == 1:
                    grid[y + 2, x] = 0.5
                    grid[y + 1, x] = 0.5
                    v -= 1
                if not y == self.height - 3:
                    y += 2
            elif dir == Directions.LEFT.value:
                if grid[y, x - 2] == 1:
                    grid[y, x - 2] = 0.5
                    grid[y, x - 1] = 0.5
                    v -= 1
                if not x == 2:
                    x -= 2
            elif dir == Directions.RIGHT.value:
                if grid[y, x + 2] == 1:
                    grid[y, x + 2] = 0.5
                    grid[y, x + 1] = 0.5
                    v -= 1
                if not x == self.width - 3:
                    x += 2
