"""Dad Joke Showdown — make.fun bounty entry.

Writes the chosen single dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output when the env var is unset), then reads the file back
and fails loudly if the bytes on disk differ from the joke.
"""

import os
import sys

JOKE = "I told my suitcase there would be no vacation this year. Now I'm dealing with emotional baggage."


def main() -> int:
    if not 1 <= len(JOKE) <= 200:
        print(f"error: joke is {len(JOKE)} characters, must be 1-200", file=sys.stderr)
        return 1

    if any(c in JOKE for c in ("\n", "\r")):
        print("error: joke must be a single line (no newline characters)", file=sys.stderr)
        return 1

    if JOKE != JOKE.strip():
        print("error: joke must not start or end with whitespace", file=sys.stderr)
        return 1

    if JOKE.count(".") != 2:
        print("error: joke must be exactly two sentences (setup + punchline)", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    with open(path, "rb") as f:
        on_disk = f.read()

    if on_disk != JOKE.encode("utf-8"):
        print("error: bytes on disk differ from the joke", file=sys.stderr)
        return 1

    print(f"wrote {len(JOKE)}-character dad joke to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
