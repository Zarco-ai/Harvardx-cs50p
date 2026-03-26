
def main():
    f = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
            }
    y = 0
    while True:
        try:
            x = input("item: ").title()
        except EOFError:
            print("Please try again\n")
            break

        if x in f:
            y += f[x]
            print(f"Total: ${y:.2f}")
        else:
            continue


main()
