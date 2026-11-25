#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes the one line a smart fridge texts its owner at 3am to
/output/entry.txt. Standard library only.
"""

import os

ENTRY_TEXT = "You promised the diet starts Monday. It is 3am on a Tuesday. I have the receipts, and the cheesecake."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 140


def main():
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError("entry must be 1 to 140 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY_TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
