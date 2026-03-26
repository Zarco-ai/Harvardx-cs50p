def main():
    n = input("Say something: " )
    convert(n)

def convert(j):
    j = j.replace(":)", "🙂")
    j = j.replace(":(", "🙁")
    print(j)
main()


