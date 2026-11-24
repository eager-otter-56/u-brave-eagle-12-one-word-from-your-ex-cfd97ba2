#!/usr/bin/env python3
"""One Word From Your Ex.

Writes exactly one word to entry.txt: the word an ex would use to
describe the entrant. One word, no punctuation, no trailing newline.
"""

import os

ENTRY = "forgettable"


def main() -> None:
    # Gate: entry.txt must be UTF-8, 1-24 chars, exactly one word.
    assert 1 <= len(ENTRY) <= 24, "entry length out of gate"
    assert len(ENTRY.split()) == 1, "entry must be exactly one word"
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
