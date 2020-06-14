import pytest
from backtracking import Backtracking
from aldous_broder import Aldous_Broder
from hunt_and_kill import Hunt_and_Kill
from prims import Prims


def test_backtracking():
    backtracking = Backtracking(201, 201, "maze.png", False)
    assert backtracking.createMaze() == 0


def test_aldous_broder():
    aldous_broder = Aldous_Broder(201, 201, "maze.png", False)
    assert aldous_broder.createMaze() == 0


def test_hunt_and_kill():
    hunt_and_kill = Hunt_and_Kill(201, 201, "maze.png", False)
    assert hunt_and_kill.createMaze() == 0


def test_prims():
    prims = Prims(201, 201, "maze.png", False)
    assert prims.createMaze() == 0
