def main():
    while True:
        try:
            h = input("Fraction: ")
            percentage_int = convert(h)
            t = gauge(percentage_int)
            print(t)
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    try:
        x_str, y_str = fraction.split('/')
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x < 0 or x > y:
        raise ValueError
    percentage = round((x / y) * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
