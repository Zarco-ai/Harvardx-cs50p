import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regex to capture 4 groups of digits separated by dots
    # We use ^ and $ to ensure we match the ENTIRE string
    regex = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.search(regex, ip)

    if match:
        # Check if each group is between 0 and 255
        for group in match.groups():
            if int(group) > 255:
                return False
        return True

    return False

if __name__ == "__main__":
    main()
