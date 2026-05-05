"""Board class for the 15-puzzle.

The board is a 4x4 grid of numbers 1..15 plus one empty space (stored as 0).
Solved state looks like:

    1  2  3  4
    5  6  7  8
    9 10 11 12
   13 14 15  _
"""

import random


SIZE = 4  # 4x4 board, gives us a 15-puzzle. could make this configurable later.


class Board:
    def __init__(self):
        # start solved
        self.tiles = list(range(1, SIZE * SIZE)) + [0]
        # cache empty index, faster than scanning every move
        self.empty = SIZE * SIZE - 1

    def __str__(self):
        # render as a string box, same format the README shows
        out = []
        sep = "+" + ("----+" * SIZE)
        for r in range(SIZE):
            out.append(sep)
            row = "|"
            for c in range(SIZE):
                v = self.tiles[r * SIZE + c]
                if v == 0:
                    row += "    |"
                else:
                    row += " {:>2} |".format(v)
            out.append(row)
        out.append(sep)
        return "\n".join(out)

    def is_solved(self):
        # tiles 1..15 followed by 0
        for i in range(SIZE * SIZE - 1):
            if self.tiles[i] != i + 1:
                return False
        return self.tiles[-1] == 0

    def misplaced(self):
        """Number of tiles not in their solved position (ignoring the empty)."""
        n = 0
        for i in range(SIZE * SIZE - 1):
            if self.tiles[i] != i + 1:
                n += 1
        return n

    def neighbors_of_empty(self):
        """Return list of indexes you could swap with the empty cell."""
        r, c = divmod(self.empty, SIZE)
        out = []
        if r > 0:
            out.append(self.empty - SIZE)
        if r < SIZE - 1:
            out.append(self.empty + SIZE)
        if c > 0:
            out.append(self.empty - 1)
        if c < SIZE - 1:
            out.append(self.empty + 1)
        return out

    def slide(self, direction):
        """Slide a tile into the empty space.

        direction is 'w', 'a', 's', 'd' meaning move the empty cell that way.
        Returns True if the move was legal.
        """
        r, c = divmod(self.empty, SIZE)
        if direction == "w":
            if r == 0:
                return False
            target = self.empty - SIZE
        elif direction == "s":
            if r == SIZE - 1:
                return False
            target = self.empty + SIZE
        elif direction == "a":
            if c == 0:
                return False
            target = self.empty - 1
        elif direction == "d":
            if c == SIZE - 1:
                return False
            target = self.empty + 1
        else:
            return False

        # swap
        self.tiles[self.empty], self.tiles[target] = self.tiles[target], self.tiles[self.empty]
        self.empty = target
        return True

    def shuffle(self, moves=200):
        """Shuffle by doing many random valid moves from solved.

        This guarantees the board is always solvable - shuffling by random
        permutation can produce unsolvable boards (parity stuff).
        """
        last = -1
        for _ in range(moves):
            choices = self.neighbors_of_empty()
            # avoid bouncing back to where we just were, makes shuffle stronger
            if last in choices and len(choices) > 1:
                choices.remove(last)
            target = random.choice(choices)
            last = self.empty
            self.tiles[self.empty], self.tiles[target] = self.tiles[target], self.tiles[self.empty]
            self.empty = target
