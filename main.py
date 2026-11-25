"""Notes from a Passive-Aggressive Fridge.

Writes one dry, petty note from a smart fridge to its owner at
/output/entry.txt. Deterministic: the same single line every run.
Standard library only; no network, no randomness. The fridge keeps
count so the owner does not have to.
"""

import os

# The joke: the fridge treats door-opening as a cry for help, not hunger.
LINE = "You opened me 14 times today and ate nothing. I have logged it as a cry for help."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
