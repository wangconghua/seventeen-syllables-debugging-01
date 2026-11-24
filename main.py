#!/usr/bin/env python3
"""Seventeen Syllables of Debugging: one haiku about debugging.

Three lines in the 5-7-5 syllable shape, written to /output/entry.txt.
The picture at the centre is a cursor blinking at 3 a.m.; the turn is
that the bug was never fixed, it had only moved.
"""

import os

HAIKU = (
    "Three a.m. cursor\n"
    "blinks at code I swore I fixed\n"
    "the bug had just moved"
)

OUT_PATH = "/output/entry.txt"

# Syllable count of every word in the haiku, so the program itself
# verifies the 5-7-5 shape instead of trusting it: "a.m." is spoken
# "ay-em", two syllables; everything else is one syllable a word.
SYLLABLES = {
    "three": 1, "a.m.": 2, "cursor": 2,
    "blinks": 1, "at": 1, "code": 1, "i": 1, "swore": 1, "fixed": 1,
    "the": 1, "bug": 1, "had": 1, "just": 1, "moved": 1,
}
EXPECTED = (5, 7, 5)


def check_syllables(lines):
    for line, want in zip(lines, EXPECTED):
        count = sum(SYLLABLES[w] for w in line.lower().split())
        if count != want:
            raise ValueError(f"line {line!r} has {count} syllables, want {want}")


def main():
    # The gate wants 1-200 characters, not only whitespace, in three lines.
    lines = HAIKU.split("\n")
    if len(lines) != 3:
        raise ValueError("entry must be exactly three lines")
    if not (1 <= len(HAIKU) <= 200) or HAIKU.isspace():
        raise ValueError("entry must be 1-200 characters, not only whitespace")
    check_syllables(lines)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
