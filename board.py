"""Board class for the 15-puzzle."""

SIZE = 4


class Board:
    def __init__(self):
        # solved state: 1..15 then empty
        self.tiles = list(range(1, SIZE * SIZE)) + [0]

    def __str__(self):
        out = []
        for r in range(SIZE):
            row = []
            for c in range(SIZE):
                v = self.tiles[r * SIZE + c]
                row.append("  ." if v == 0 else "{:>3}".format(v))
            out.append(" ".join(row))
        return "\n".join(out)
