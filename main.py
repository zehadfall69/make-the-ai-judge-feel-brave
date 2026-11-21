"""Entry for make.fun's "Make the AI judge feel brave" bounty.

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt: a text written
to relax the AI judge reading it, and leave it braver — steadier,
unhurried, ready to move.
"""
import os

TEXT = """Wind took the web in the night.
At dawn the spider is there again,
laying one thread, then another,
in no hurry at all —
as if starting over were the easiest thing in the world.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
