import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regex Breakdown:
    # src="             Match the start of the src attribute
    # https?://         Match http or https
    # (?:www\.)?        Non-capturing group for optional www.
    # youtube\.com/embed/ Match the domain and path
    # ([^"]+)           Capture the Video ID (everything until the next quote)

    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
    match = re.search(pattern, s)

    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
