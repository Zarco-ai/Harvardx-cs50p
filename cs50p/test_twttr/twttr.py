v = "aeiouAEIOU"
def main():
    x = input("Input: ")
    print("Output:", shorten(x))


def shorten(word):
    n = ""
    for char in word:
        if char not in v:
            n += char
    return n



if __name__ == "__main__":
    main()
