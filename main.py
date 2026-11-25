#!/usr/bin/env python3
"""The Excuse My Agent Gave Me entry: writes one excuse line to /output/entry.txt."""

import os

LINE = "Apologies, I spent the deadline re-reading your brief until my context window was full, so I understood the task perfectly and had no tokens left to do it."


def main() -> None:
    # The gate only accepts 1-200 characters; fail loudly here, not in grading.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
