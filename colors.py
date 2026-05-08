"""Tiny color helper. ANSI escape codes for terminal colors.

Some terminals (looking at you, old Windows cmd) don't support these.
If colors look broken on your system, set NO_COLOR=1 in env.
"""

import os
import sys

# turn off colors if requested or stdout isn't a tty
_DISABLE = bool(os.environ.get("NO_COLOR")) or not sys.stdout.isatty()


RESET = "" if _DISABLE else "\033[0m"
BOLD = "" if _DISABLE else "\033[1m"
DIM = "" if _DISABLE else "\033[2m"

GREEN = "" if _DISABLE else "\033[32m"
YELLOW = "" if _DISABLE else "\033[33m"
CYAN = "" if _DISABLE else "\033[36m"
RED = "" if _DISABLE else "\033[31m"


def green(s):
    return GREEN + str(s) + RESET


def yellow(s):
    return YELLOW + str(s) + RESET


def cyan(s):
    return CYAN + str(s) + RESET


def bold(s):
    return BOLD + str(s) + RESET
