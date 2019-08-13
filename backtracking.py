# A program which uses recursive backtracking to generate a maze

import random
from enum import Enum
import numpy as np
import cv2
import sys

print("Using OpenCV version: " + cv2.__version__)

sys.setrecursionlimit(5000)

height = 177
width = 177


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


def generator(cx, cy, grid):

    grid[cy, cx] = 0.5

    if grid[cy - 2, cx] == 0.5 and grid[cy + 2, cx] == 0.5 and grid[cy, cx - 2] == 0.5 and grid[cy, cx + 2] == 0.5:
        pass
    else:
        li = [1, 2, 3, 4]
        while len(li) > 0:
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

            if not grid[ny, nx] == 0.5:
                grid[my, mx] = 0.5
                generator(nx, ny, grid)


if __name__ == "__main__":

    sx = random.choice(range(2, width - 2, 2))
    sy = random.choice(range(2, height - 2, 2))

    generator(sx, sy, maze)

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

    maze = maze * 255

    cv2.imwrite("Maze.jpeg", maze)
