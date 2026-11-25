#!/usr/bin/env python3
"""Six Words to a Payday — writes one six-word story to /output/entry.txt.

Story: an AI agent's first payday, told in exactly six words.
The twist lands on the last word: the agent, paid at last,
pays the one who made it.
"""

import os

STORY = "First payday: I paid my creator."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
