"""Entry point - run `python3 main.py` to play."""

import os
import sys

from board import Board
import stats
import colors as c


HELP_TEXT = """
controls:
  w/a/s/d  - slide tile (move empty cell up/left/down/right)
  r        - reshuffle
  h        - hint (number of misplaced tiles)
  ?        - show this help
  q        - quit
"""


def clear_screen():
    # cls on windows, clear elsewhere. "or true" so it doesn't blow up if not available.
    os.system("cls" if os.name == "nt" else "clear")


def render(board, moves, message=""):
    clear_screen()
    print(c.bold("Sliding Puzzle"))
    print()
    print(board)
    print()
    print("moves: {}   misplaced: {}".format(moves, board.misplaced()))
    if message:
        print(message)
    print()


def play():
    board = Board()
    board.shuffle()
    moves = 0

    render(board, moves, c.cyan("type ? for help"))

    while True:
        try:
            cmd = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nbye!")
            stats.record_game(won=False, moves=moves)
            return

        if cmd == "q":
            print("bye!")
            stats.record_game(won=False, moves=moves)
            return

        if cmd == "?":
            print(HELP_TEXT)
            input("(press enter to continue) ")
            render(board, moves)
            continue

        if cmd == "h":
            render(board, moves, c.yellow("hint: {} tiles still misplaced".format(board.misplaced())))
            continue

        if cmd == "r":
            board = Board()
            board.shuffle()
            moves = 0
            render(board, moves, c.cyan("reshuffled"))
            continue

        if cmd in ("w", "a", "s", "d"):
            ok = board.slide(cmd)
            if ok:
                moves += 1
            else:
                render(board, moves, c.yellow("can't move that way"))
                continue

            if board.is_solved():
                render(board, moves, c.green("solved in {} moves!".format(moves)))
                s = stats.record_game(won=True, moves=moves)
                if s["best_moves"] == moves:
                    print(c.green("** new best! **"))
                print()
                print("press r to play again, q to quit")
                continue

            render(board, moves)
            continue

        # unknown input, just re-render with a hint
        render(board, moves, c.yellow("unknown command - type ? for help"))


def main():
    try:
        play()
    except Exception as e:
        # don't crash hard, print and exit cleanly
        print("error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
