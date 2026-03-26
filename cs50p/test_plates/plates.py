import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #check plate length; no less than 2 and no greater than 6
    if len(s) >= 2 and len(s) <=6:
        pass
    else:
        return False
    for char in s:
        if not char.isalnum():
            return False
    #check first two char in plate are letters
    if s[0].isalpha() and s[1].isalpha():
        pass
    else:
        return False
    fd = -1
    for index, char in enumerate(s):
        if char.isdigit():
            fd = index
            break
    if fd == -1 :
        return True
    elif s[fd] == '0':
        return False
    else:
        for d in s[fd: ]:
            if d.isalpha():
                return False
            else:
                pass
        return True


if __name__ == "__main__":
    main()

