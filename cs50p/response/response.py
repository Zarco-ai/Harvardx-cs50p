from validator_collection import validators, checkers, errors

def main():
    email = input("What's your email address? ")

    # The checkers.is_email returns True/False
    # Alternatively validators.email raises an error if invalid
    if checkers.is_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
