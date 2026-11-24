#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give
(<=140 chars) to /output/entry.txt. Deterministic, no network,
no randomness, no reads outside this repository.
"""

import os

LINE = "If your car battery dies, jump-start it with a toaster. Both run on electricity, so the physics checks out."


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Verify the bytes on disk are exactly the line we meant to submit.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt on disk differs from LINE"


if __name__ == "__main__":
    main()
