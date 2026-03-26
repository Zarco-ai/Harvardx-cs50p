def main():
    e = input("Expression: ")
    x, y, z = e.split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        a1= x + z
        print(a1)
    elif y == "-":
        a2= x - z
        print(a2)
    elif y == "/":
        a3= x / z
        print(a3)
    elif y == "*":
        a4= x * z
        print(a4)
main()
