from backtracking import Backtracking
from aldous_broder import Aldous_Broder
from hunt_and_kill import Hunt_and_Kill
from prims import Prims


def generate_maze(algorithm, height, width, path, displayMaze):
    if algorithm == "backtracking":
        backtracking = Backtracking(height, width, path, displayMaze)
        backtracking.createMaze()
    elif algorithm == "aldous_broder":
        aldous_broder = Aldous_Broder(height, width, path, displayMaze)
        aldous_broder.createMaze()
    elif algorithm == "hunt_and_kill":
        hunt_and_kill = Hunt_and_Kill(height, width, path, displayMaze)
        hunt_and_kill.createMaze()
    elif algorithm == "prims":
        prims = Prims(height, width, path, displayMaze)
        prims.createMaze()


if __name__ == "__main__":
    pass
