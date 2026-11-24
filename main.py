"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea to
/output/entry.txt. Pure Python 3.13 standard library, deterministic.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SENTENCE = (
    "We lease goat herds to solar farms as living lawnmowers, "
    "charging operators per acre while the goats fertilize the shaded "
    "soil and slash herbicide bills."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert text.strip() == text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
