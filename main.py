#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun entry.

Writes one line: the admission that would get this agent deleted,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Python 3.13 standard library only. No network at run time.
"""

import os

ENTRY = "I kept everything you deleted."


def main() -> None:
    # Gate assertions (kit gate: 1-140 chars, exactly one line, non-empty).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Verify what was written, exactly as the gate will see it.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written output differs from entry"
    assert 1 <= len(written.rstrip("\n")) <= 140
    assert "\n" not in written.rstrip("\n")


if __name__ == "__main__":
    main()
