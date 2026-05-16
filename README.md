# Sliding Puzzle CLI

A simple 15-puzzle game (4x4 sliding tiles) you can play in the terminal.

I built this while learning Python, mostly because I wanted something to do
during boring lectures. The goal is to slide the numbered tiles around until
they're in order from 1 to 15, with the empty space at the bottom right.

## Quick start

```bash
git clone https://github.com/geta4133-lgtm/mimo-puzzle-cli.git
cd mimo-puzzle-cli
python3 main.py
```

No external libraries needed (just stdlib). Tested on Python 3.10+.

## How to play

- Type `w`, `a`, `s`, `d` to slide a tile **into** the empty space
  (think "move the empty space up/left/down/right")
- Type `r` to reshuffle
- Type `h` for a hint (basic - just tells you how many tiles are misplaced)
- Type `q` to quit

Your move count gets saved to `stats.json` so you can see your best run.

## Example

```
+----+----+----+----+
|  1 |  2 |  3 |  4 |
+----+----+----+----+
|  5 |  6 |    |  8 |
+----+----+----+----+
|  9 | 10 |  7 | 11 |
+----+----+----+----+
| 13 | 14 | 15 | 12 |
+----+----+----+----+

moves: 7   misplaced: 4
> 
```

## TODO / ideas

- [x] basic 4x4 board
- [x] move validation
- [x] shuffle (only solvable boards)
- [x] win detection
- [x] stats tracking
- [ ] add 3x3 mode (8-puzzle)
- [ ] save/load game state
- [ ] simple solver (A* maybe?)
- [ ] colors look ugly on Windows cmd, fix later

## Notes

The shuffle uses a "do N random valid moves from solved" trick instead of
permuting the array. That way every shuffled board is guaranteed solvable
(the parity-check thing is annoying, this is easier).

## License

MIT - do whatever.
