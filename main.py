import os
import sys
from board import Board


def render(board, moves):
    os.system("cls" if os.name == "nt" else "clear")
    print("Sliding Puzzle")
    print()
    print(board)
    print()
    print("moves:", moves)


def main():
    b = Board()
    b.shuffle()
    moves = 0
    render(b, moves)

    while True:
        cmd = input("> ").strip().lower()
        if cmd == "q":
            return
        if cmd in ("w", "a", "s", "d"):
            if b.slide(cmd):
                moves += 1
            if b.is_solved():
                render(b, moves)
                print("solved in", moves, "moves!")
                return
            render(b, moves)


if __name__ == "__main__":
    main()
