import sys
import random
from pyfiglet import Figlet

def main():
    #Set up figlet
    figlet = Figlet()
    fonts = figlet.getFonts()
    ac = len(sys.argv)
    #Go through command line arguments
    if ac < 3 or ac > 3:
        if ac > 3:
            sys.exit("Too many arguments")
        else:
            sys.exit("Few arguments")
    elif ac == 1:
        rf = random.choice(fonts)
        figlet.setFont(font=rf)
        print(figlet.renderText(x))
    elif ac == 3:
        c1 = sys.argv[1]
        c2 = sys.argv[2]
        if c1 != '-f' and c1 != '--font':
            sys.exit("Invalid first command-line argument")
        if c2 not in fonts:
            sys.exit("Invalid second command-line argument")
        x = input("Input: ")
        figlet.setFont(font=c2)
        print(figlet.renderText(x))
    else:
        sys.exit(0)

main()
