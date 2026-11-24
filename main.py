"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.

Normalizes at most one trailing newline (an editor may append one) before
validating, so the graded line is exact.

Competition: u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    with open(src, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    # Drop at most one trailing newline (a file editor may append one),
    # then at most one trailing CR (for a CRLF ending). Validation runs
    # on the normalized text; what gets written is the normalized text.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]
    raw = text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        sys.exit("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        sys.exit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output/")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(raw)
    os.chmod(out_path, 0o644)
    print("wrote %s (%d characters)" % (out_path, len(text)))


if __name__ == "__main__":
    main()
