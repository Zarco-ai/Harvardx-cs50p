import string
def main():
    fruit = input("Item: ")
    a = {
        "apple" : "130",
        "Avocado" : "50",
        "Sweet Cherries" : "100",
        "Kiwifruit" : "90",
        "pear" : "100",
    }
    if fruit in a:
        print("Calories:", a[fruit])
main()
