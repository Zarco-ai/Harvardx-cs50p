import inflect
def main():
    p = inflect.engine()
    nl = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            print("Adieu, adieu, to", nnl)
            break
        nl.append(name)
        nnl = p.join(nl)
main()
