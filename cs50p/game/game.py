import random
import sys
def main():
    while True:
        try:
            while True:
                try:
                    x = int(input("Level: "))
                except (ValueError):
                    continue
                if x < 1:
                    continue
                else:
                    break

            r = random.randrange(1, 1000)

            while True:
                try:
                    y = int(input("Guess: "))
                except (ValueError):
                    continue
                if y < 1:
                    continue
                elif y > r:
                    print("Too large!")
                    continue
                elif y < r:
                    print("Too Small!")
                    continue
                else:
                    print("Just right!")
                    sys.exit()

        except EOFError:
            break
main()
