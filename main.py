"""Entry for make.fun: The Word You'd Delete From the Dictionary.

The pick: "word" -- a dictionary is a book of words, so erasing the
word "word" leaves it unable to name what it contains.
"""

import os

# The one word to erase: "word". A dictionary is a book of words, so
# deleting it leaves the dictionary unable to name what it contains.
ENTRY = "word"


def main() -> None:
    # The gate allows 1-77 characters and the judge wants exactly one
    # word with nothing added around it: no trailing newline, no spaces.
    assert ENTRY and len(ENTRY) <= 77 and len(ENTRY.split()) == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
