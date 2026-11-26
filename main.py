"""The Internet in One Word — make.fun entry.

Writes the chosen one-word description of the whole internet to
/output/entry.txt. The word is "Doomscroll": funny on its own, true of
the internet as a whole (the compulsive endless scroll is its defining
behaviour), and surprising next to the obvious words.
"""

import os

ENTRY = "Doomscroll"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
