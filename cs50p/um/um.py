import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # \b matches word boundaries.
    # We count occurrences of "um" surrounded by boundaries.
    # re.IGNORECASE makes it match "Um", "UM", "um".
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))

if __name__ == "__main__":
    main()
