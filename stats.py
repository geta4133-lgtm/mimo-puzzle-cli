"""Stats tracking - keep best move count across runs."""

import json
import os

STATS_FILE = "stats.json"


def load():
    if not os.path.exists(STATS_FILE):
        return {"games_played": 0, "games_won": 0, "best_moves": None}
    try:
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # file got corrupted or unreadable, start fresh
        return {"games_played": 0, "games_won": 0, "best_moves": None}


def save(stats):
    try:
        with open(STATS_FILE, "w") as f:
            json.dump(stats, f, indent=2)
    except OSError as e:
        # not fatal, just skip
        print("warning: couldn't save stats:", e)


def record_game(won, moves):
    """Update stats after a finished game."""
    s = load()
    s["games_played"] += 1
    if won:
        s["games_won"] += 1
        if s["best_moves"] is None or moves < s["best_moves"]:
            s["best_moves"] = moves
    save(s)
    return s
