"""Board class for the 15-puzzle."""

SIZE = 4


class Board:
    def __init__(self):
        self.tiles = list(range(1, SIZE * SIZE)) + [0]
        self.empty = SIZE * SIZE - 1

    def __str__(self):
        out = []
        for r in range(SIZE):
            row = []
            for c in range(SIZE):
                v = self.tiles[r * SIZE + c]
                row.append("  ." if v == 0 else "{:>3}".format(v))
            out.append(" ".join(row))
        return "\n".join(out)

    def slide(self, direction):
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

        self.tiles[self.empty], self.tiles[target] = self.tiles[target], self.tiles[self.empty]
        self.empty = target
        return True
