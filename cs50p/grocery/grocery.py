
def main():
    y = {}

    while True:
        try:
            s = input("").upper()
            if s in y:
                y[s] += 1
            else:
                y[s] = 1
        except EOFError:
            for item in sorted(y.keys()):
        # Retrieve the count for the current item
                count = y[item]
        # Print the final output in the format: COUNT ITEM_NAME
                print(f"{count} {item}")
            break
        else:
            continue


main()


















main()
