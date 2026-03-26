import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1) # Or just exit regex gracefully

def convert(s):
    # Regex supports "9:00 AM" and "9 AM"
    # Group 1: Start Hour, Group 2: Start Minute (optional), Group 3: AM/PM
    # Group 4: End Hour,   Group 5: End Minute (optional),   Group 6: AM/PM
    regex = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(regex, s)

    if not match:
        raise ValueError

    # Unpack groups
    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    # Helper to convert individual time
    time1 = to_24_hour(start_hour, start_min, start_period)
    time2 = to_24_hour(end_hour, end_min, end_period)

    return f"{time1} to {time2}"

def to_24_hour(hour, minute, period):
    h = int(hour)
    # Default minutes to 00 if not present
    m = int(minute) if minute else 0

    # Validate Ranges
    if not (1 <= h <= 12) or not (0 <= m < 60):
        raise ValueError

    if period == "PM" and h != 12:
        h += 12
    elif period == "AM" and h == 12:
        h = 0

    return f"{h:02}:{m:02}"

if __name__ == "__main__":
    main()
