# A program which uses Aldous-Broder Algorithm to generate a maze

import random
from enum import Enum
import numpy as np
import cv2

print("Using OpenCV version: " + cv2.__version__)

height = 113
width = 113

class Directions(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

maze = np.ones((height, width), dtype=np.float)

for i in range(height):
    for j in range(width):
        if i % 2 == 1 or j % 2 == 1:
            maze[i, j] = 0
        if i == 0 or j == 0 or i == height - 1 or j == width - 1:
            maze[i, j] = 0.5



def aldous_broder(x, y, grid):

    grid[y, x] = 0.5

    v = ((height - 5)/2 + 1) * ((width - 5)/2 + 1)
    print(v)

    # while all cells have not been visited
    while v > 1:

        print(v)

        dir = random.randint(1, 4)
    
        if dir == Directions.UP.value:
            if grid[y - 2, x] == 1:
                grid[y - 2, x] = 0.5
                grid[y - 1, x] = 0.5
                v = v - 1
            if not y == 2:
                y = y - 2
        elif dir == Directions.DOWN.value:
            if grid[y + 2, x] == 1:
                grid[y + 2, x] = 0.5
                grid[y + 1, x] = 0.5
                v = v - 1
            if not y == height - 3:
                y = y + 2
        elif dir == Directions.LEFT.value:
            if grid[y, x - 2] == 1:
                grid[y, x - 2] = 0.5
                grid[y , x - 1] = 0.5
                v = v - 1
            if not x == 2:
                x = x - 2
        elif dir == Directions.RIGHT.value:
            if grid[y, x + 2] == 1:
                grid[y, x + 2] = 0.5
                grid[y, x + 1] = 0.5
                v = v - 1
            if not x == width - 3:
                x = x + 2


if __name__ == "__main__":
    
    sx = random.choice(range(2, width - 2, 2))
    sy = random.choice(range(2, height - 2, 2))
    
    aldous_broder(sx, sy, maze)


    for i in range(height):
        for j in range(width):
            if not maze[i, j] == 0:
                maze[i, j] = 1

    maze[1, 2] = 1
    maze[height - 2, width - 3] = 1

    cv2.namedWindow('Maze', cv2.WINDOW_NORMAL)
    cv2.imshow('Maze', maze)
    cv2.waitKey(0)
    cv2.destroyAllWindows()