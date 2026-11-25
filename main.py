#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line to /output/entry.txt.

The fortune was chosen for a crypto trader who has just been
liquidated, reading a cookie at 3am with an empty wallet and a
stubborn sense of humour. The classic fortune-cookie line
"Your lucky numbers are ..." is kept, the numbers are all
zero -- the empty balance -- and the punchline lands on the
one thing the liquidation could not take: the friend who
texts back at 3am.

Deterministic: the same single line is written on every run.
"""

import os

FORTUNE = (
    "Your lucky numbers are 0.00, 0.00, 0.00, "
    "and the friend who texts back at 3am."
)

# Gate the entry against the competition's own limits before writing:
# at most 20 words, 1-160 characters of UTF-8 text.
assert 1 <= len(FORTUNE.split()) <= 20
assert 1 <= len(FORTUNE.encode("utf-8")) <= 160


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
