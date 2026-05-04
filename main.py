import os
from board import Board


def main():
    b = Board()
    while True:
        os.system("clear")
        print(b)
        cmd = input("> ").strip().lower()
        if cmd == "q":
            break
        b.slide(cmd)


if __name__ == "__main__":
    main()
