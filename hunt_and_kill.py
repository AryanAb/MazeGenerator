# A maze solving algorith which uses hunt and kill
# It might be possible to improve this algorithm by moving the function calls outside of the functions

import cv2
import numpy as np
from enum import Enum
import random
import sys

sys.setrecursionlimit(8000)

print("Using OpenCV version: " + cv2.__version__)

height = 277
width = 277


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
            maze[i, j] = 0.3


def kill(cx, cy, grid):

    print("Killing")

    grid[cy, cx] = 0.5

    trapped = False

    while not trapped:

        if grid[cy - 2, cx] <= 0.5 and grid[cy + 2, cx] <= 0.5 and grid[cy, cx - 2] <= 0.5 and grid[cy, cx + 2] <= 0.5:
            trapped = True
            print("Trapped")
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

                if grid[ny, nx] != 0.5 and grid[ny, nx] != 0.3:
                    grid[my, mx] = 0.5
                    cy = ny
                    cx = nx
                    grid[cy, cx] = 0.5
                    break

    hunt(grid)


def hunt(grid):

    print("Hunting")

    neighbor = []

    for i in range(2, height - 2, 2):
        for j in range(2, width - 2, 2):

            if grid[i, j] == 1:

                if grid[i - 2, j] == 0.5:
                    neighbor.append(Directions.UP.value)
                if grid[i + 2, j] == 0.5:
                    neighbor.append(Directions.DOWN.value)
                if grid[i, j - 2] == 0.5:
                    neighbor.append(Directions.LEFT.value)
                if grid[i, j + 2] == 0.5:
                    neighbor.append(Directions.RIGHT.value)

                if len(neighbor) > 0:
                    _dir = random.choice(neighbor)

                    if _dir == Directions.UP.value:
                        grid[i - 1, j] = 0.5
                    elif _dir == Directions.DOWN.value:
                        grid[i + 1, j] = 0.5
                    elif _dir == Directions.LEFT.value:
                        grid[i, j - 1] = 0.5
                    elif _dir == Directions.RIGHT.value:
                        grid[i, j + 1] = 0.5
                    kill(j, i, grid)


sx = random.choice(range(2, width - 2, 2))
sy = random.choice(range(2, height - 2, 2))

kill(sx, sy, maze)

for i in range(height):
    for j in range(width):
        if maze[i, j] != 0:
            maze[i, j] = 1

    maze[1, 2] = 1
    maze[height - 2, width - 3] = 1

cv2.namedWindow('Maze', cv2.WINDOW_NORMAL)
cv2.imshow('Maze', maze)
cv2.waitKey(0)
cv2.destroyAllWindows()
