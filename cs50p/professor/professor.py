import random
import sys

def main():

    l = get_level()
    count = 0

    for _ in range(10):                 ###
        x = generate_integer(l)
        y = generate_integer(l)
        result = x + y
        corr = False                    ###
        for attempt in range(3):
            try:
                ui = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
            if ui == result:
                corr = True             ###
                if attempt == 0:        ###
                    count += 1
                break
            else:
                if attempt < 2:
                    print("EEE")
        if corr:
            continue
        else:
            print(f"{x} + {y} = {result}")
    print(f"Score: {count}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level not in [1, 2, 3]: ###
            continue
        else:
            return level


def generate_integer(level):            ###
    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    elif level == 3:
        return random.randrange(100, 1000)

if __name__ == "__main__":
    main()
