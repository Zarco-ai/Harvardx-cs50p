import csv
import sys
from tabulate import tabulate

def main():
    c = []
   #Command Line Argument
    if len(sys.argv) !=2:
      sys.exit("Too many/few arguments!")
    elif sys.argv[1].endswith('.csv') == False :
      sys.exit("Does not end with '.py'")
    else:
      f = sys.argv[1]

    #File stuff
    try:
        with open(f) as file:
            reader = csv.reader(file)
            for row in reader:
                c.append([row[0], row[1], row[2]])
    except FileNotFoundError:
       sys.exit("File does not exsist...")
    print(tabulate(c, headers="firstrow", tablefmt="grid"))

main()
