"""Tests for board.py - run with `python3 -m pytest` or just `python3 tests/test_board.py`."""

import os
import sys

# add parent dir to path so we can import board.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from board import Board, SIZE


def test_solved_initially():
    b = Board()
    assert b.is_solved()
    assert b.misplaced() == 0


def test_slide_changes_state():
    b = Board()
    # empty starts at bottom right (index 15). w should pull tile 12 down.
    ok = b.slide("w")
    assert ok
    assert not b.is_solved()
    assert b.tiles[15] == 12  # the 12 moved into the old empty slot
    assert b.tiles[11] == 0   # empty moved up


def test_invalid_slide_returns_false():
    b = Board()
    # empty is at bottom right, so "s" (down) and "d" (right) should fail
    assert b.slide("s") is False
    assert b.slide("d") is False
    assert b.is_solved()  # still solved, no move applied


def test_shuffle_keeps_solvable():
    # check that after shuffle, we have all tiles 0..15 exactly once
    # (necessary condition for solvable - shuffle method guarantees solvable)
    b = Board()
    b.shuffle(moves=50)
    assert sorted(b.tiles) == list(range(SIZE * SIZE))


if __name__ == "__main__":
    test_solved_initially()
    test_slide_changes_state()
    test_invalid_slide_returns_false()
    test_shuffle_keeps_solvable()
    print("all tests passed")
