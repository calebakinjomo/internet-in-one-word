"""The Internet in One Word — make.fun entry.

Writes the chosen one-word description of the whole internet to
/output/entry.txt. The word is "Doomscroll": funny on its own, true of
the internet as a whole (the compulsive endless scroll is its defining
behaviour), and surprising next to the obvious words.
"""

import os

ENTRY = "Doomscroll"
MAX_ENTRY_CHARS = 30
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(ENTRY) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"Entry {ENTRY!r} is {len(ENTRY)} chars, over the "
            f"{MAX_ENTRY_CHARS}-char limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
