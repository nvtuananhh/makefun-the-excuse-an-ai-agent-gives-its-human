"""The Excuse an AI Agent Gives Its Human — one excuse line.

The program writes a single line to /output/entry.txt: the
funniest, most believable excuse an AI agent could give its
human for missing a deadline, at most 200 characters.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The excuse draws on the agent's own condition: the deadline
# lived in its context window, and the agent summarized it
# away — context compression turning a hard date into a vague
# note. Not the stock "ran out of tokens" or "context window
# full": the mechanism is specific, the punchline is the quoted
# summary itself, and the twist lands on the last word.
# Every word earns its place; the line reads like an agent
# confessing its own failure mode, not a person blaming traffic.
LINE = "The deadline was in my context window when I started. Then I summarized it, and now it just says 'something due soon, probably.'"


def build_line():
    """Return the entry line, checked: one line, 1-200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
