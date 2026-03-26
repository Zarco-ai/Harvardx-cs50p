a = 50
while a > 0:
    print(f"Amount Due: {a}")
    # get coin amount
    x = int(input("Insert Coin: "))
    # verify coin amount
    while x not in (1, 5, 10, 25):
        print(f"Amount Due: {a}")
        x = int(input("Insert Coin: "))
    # subtract coin amount from amount due
    a = a - x
    if a < 0:
        c = a * -1
        print(f"Change Owed: {c}")
    elif a == 0:
        print("Change Owed: 0")


