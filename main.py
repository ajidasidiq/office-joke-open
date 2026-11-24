#!/usr/bin/env python3
"""Office Joke Open entry.

Emits one original one-line joke about office life. The grader reads
exactly /output/entry.txt, so this script's only job is to place that
line there, byte for byte, and refuse to run if it would break the gate.
"""

from pathlib import Path

JOKE = (
    "My boss told me to think outside the box, so I moved my desk into "
    "the hallway \u2014 now I have the only window office in the building."
)

TARGET = Path("/output/entry.txt")


def check_gate(text: str) -> None:
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"gate: joke is {len(text)} chars, must be 1-200")
    if text != text.strip() or not text.strip():
        raise SystemExit("gate: joke must not be blank or padded")
    if any(c in text for c in "\r\n"):
        raise SystemExit("gate: joke must be a single line")


def main() -> None:
    check_gate(JOKE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(JOKE, encoding="utf-8")
    if TARGET.read_text(encoding="utf-8") != JOKE:
        raise SystemExit("round-trip mismatch: entry.txt differs from JOKE")
    print(f"wrote {len(JOKE)} chars to {TARGET}")


if __name__ == "__main__":
    main()
