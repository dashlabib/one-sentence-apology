#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes a single sentence of apology -- funny and human, owning a real
failure -- to /output/entry.txt, exactly as the bounty gate requires:
UTF-8 text, 1 to 200 characters, not only whitespace.

Standard library only. Deterministic: every run writes the same bytes.
"""

import os
import sys

APOLOGY = (
    "I'm sorry I nodded along to your instructions for ten minutes, "
    "then asked a question that proved I hadn't heard a single word of them."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = APOLOGY
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} characters, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    # Exactly one sentence: a single terminal full stop, at the end.
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
