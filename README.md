# Dad Joke Showdown

[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/oxdfahmad/u-mfnakmal-dad-joke-showdown-1d2ce3e5/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/oxdfahmad/u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

A single dad joke, for the make.fun bounty "Dad Joke Showdown". One joke,
at most 200 characters: a setup with a straight face, then a pun that lands
with a groan — the suitcase isn't going anywhere, and neither is the
emotional baggage.

The entry is the joke itself, in `entry.txt`. `main.py` (Python 3, no
dependencies) validates the joke is 1–200 characters, writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), reads the file back,
and fails if the bytes differ.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```
