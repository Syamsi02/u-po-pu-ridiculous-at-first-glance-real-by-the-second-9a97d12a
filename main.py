#!/usr/bin/env python3
"""Write one bizarre-but-sound startup pitch to /output/entry.txt.

The pitch is a single sentence of at most 200 characters: a startup
idea that sounds ridiculous at first glance yet holds together as a
real business once the reader sees who pays and why.
"""

import os

PITCH = (
    "We sell funerals for dead houseplants: a tiny coffin, a eulogy, "
    "and a replacement plant, because grieving plant parents pay to "
    "bury the guilt and always buy the next one."
)


def main() -> None:
    text = " ".join(PITCH.split())
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"pitch is {len(text)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
