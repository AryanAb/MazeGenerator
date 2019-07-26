# A program which uses recursive backtracking to generate a maze

import random
from enum import Enum
import numpy as np
import cv2
import sys

print("Using OpenCV version: " + cv2.__version__)

sys.setrecursionlimit(5000)

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


def generator(cx, cy, grid , li):

    grid[cy, cx] = 0.5

    if grid[cy - 2, cx] == 0.5 and grid[cy + 2, cx] == 0.5 and grid[cy, cx - 2] == 0.5 and grid[cy, cx + 2] == 0.5:
        pass
    else:
        #dir = randint(1, 4)
        dir = random.choice(li)
        li.remove(dir)

        if dir == Directions.UP.value:
            ny = cy - 2
            my = cy - 1
        elif dir == Directions.DOWN.value:
            ny = cy + 2
            my = cy + 1
        else:
            ny = cy
            my = cy

        if dir == Directions.LEFT.value:
            nx = cx - 2
            mx = cx - 1
        elif dir == Directions.RIGHT.value:
            nx = cx + 2
            mx = cx + 1
        else:
            nx = cx
            mx = cx

        if 0 < nx < width and 0 < ny < height and not grid[ny, nx] == 0.5:
            grid[my, mx] = 0.5
            generator(nx, ny, grid, [1, 2, 3, 4])
        else:
            generator(cx, cy, grid, li)
        generator(cx, cy, grid, [1, 2, 3, 4])

if __name__ == "__main__":
    
    sx = random.choice(range(2, width - 2, 2))
    sy = random.choice(range(2, height - 2, 2))

    generator(sx,sy, maze, [1, 2, 3, 4])

    for i in range(height):
        for j in range(width):
            if maze[i, j] == 0.5:
                maze[i, j] = 1

    maze[1, 2] = 1
    maze[height - 2, width - 3] = 1

    cv2.namedWindow('Maze', cv2.WINDOW_NORMAL)
    cv2.imshow('Maze', maze)
    cv2.waitKey(0)
    cv2.destroyAllWindows()