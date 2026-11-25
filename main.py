#!/usr/bin/env python3
"""Writes one joke about a meeting that should have been an email.

The line: the meeting's only outcome was an email summarizing the meeting
that should have been an email. The turn lands on the last word, and the
recursion is the joke -- the meeting produced the very email it should
have been, which is also exactly what real meetings do.
"""

import os

LINE = "The meeting's only outcome was an email summarizing the meeting that should have been an email."


def validate(line: str) -> None:
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    # One sentence only: no sentence-ending punctuation before the final char.
    if any(c in line[:-1] for c in ".!?"):
        raise ValueError("entry must be a single sentence")
    # The joke must name both halves of the brief.
    if "meeting" not in line.lower() or "email" not in line.lower():
        raise ValueError("entry must mention both the meeting and the email")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
