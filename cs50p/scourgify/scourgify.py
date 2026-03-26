import csv
import sys

def main():
    c = []
    #Command Line Argument
    if len(sys.argv) !=3:
      sys.exit("Too many/few arguments!")
    if not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('.csv'):
      sys.exit("Does not end with '.py'")
    else:
      f = sys.argv[1]
      t = sys.argv[2]

    #File Manipulation:
    #1st, open the file and add all content to a list to make content of file editable
    try:
        with open(f) as file:
            reader = csv.DictReader(file) ###Write about DictReader
            for row in reader:
                c.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File does not exsist...")

    #2nd, take every dict in c, and for each value of key,"name", switch the order of names from first to last
    ###Write about this section###
    o = []
    for i in c:
        #Get the first and last name
        k = i["name"]
        last, first = k.split(",")
        o.append({
            "first": first.strip(),
            "last": last.strip(),
            "house": i["house"]
        })
        #Write to the File
        ###Write about this section###
    try:
        with open(t, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader() #Needed for Check50
            writer.writerows(o)
    except FileNotFoundError:
        sys.exit(f"Could not write to {t}")


main()
