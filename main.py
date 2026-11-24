"""One Word From Your Ex — entry program.

Writes exactly one word to /output/entry.txt: the word the
entrant's ex would use to describe them.
"""

import os

WORD = "practice"  # the word my ex would use to describe me: just practice


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
