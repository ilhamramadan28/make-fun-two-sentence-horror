#!/usr/bin/env python3
"""Two-Sentence Horror - write entry.txt to /output/entry.txt."""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
OUT = "/output/entry.txt"


def main() -> int:
    with open(SRC, "r", encoding="utf-8") as f:
        text = f.read()
    # Guard: the gate is exactly two sentences, 1-400 chars of UTF-8,
    # not only whitespace, one line. Two sentences = exactly two periods.
    stripped = text.strip()
    if not 1 <= len(text) <= 400 or not stripped or "\n" in stripped:
        print("entry fails gate: must be 1-400 chars, not only whitespace, one line",
              file=sys.stderr)
        return 1
    if text.count(".") != 2 or not text.endswith("."):
        print("entry fails gate: must be exactly two sentences",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    os.chmod(OUT, 0o644)
    with open(SRC, "rb") as a, open(OUT, "rb") as b:
        if a.read() != b.read():
            print("byte-verify failed", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
