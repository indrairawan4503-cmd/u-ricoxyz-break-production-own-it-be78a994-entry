"""Break Production, Own It — variant B.

The one line an AI agent prints the instant it breaks production:
a Friday deploy, zero tests, runbook followed to the letter, prod
down anyway. Writes the line to the grader output directory first,
then best-effort mirrors it next to this file for local inspection.
"""

import os

ENTRY = (
    "I ran zero tests, shipped straight to production on a Friday at "
    "4:59pm, and followed the deploy runbook to the letter \u2014 "
    "checkout is down, every order is failing, and the runbook still "
    "says ship it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    try:
        # Best-effort mirror next to this file (not the cwd), so local
        # runs leave a readable copy; the grader mounts the repo
        # read-only, so a failure here must never sink the run.
        mirror = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(mirror, "w", encoding="utf-8") as handle:
            handle.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
