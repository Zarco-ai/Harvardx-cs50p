import sys
import string


def main():
   #expect one cla, the name of a python file
    if len(sys.argv) !=2:
      sys.exit("Too many/few arguments!")
    elif sys.argv[1].endswith('.py') == False :
      sys.exit("Does not end with '.py'")
    else:
      f = sys.argv[1]
    #output number of lines of code in file, excluding comments and blank lines
    try:
        with open(f) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exsist...")
    cc = 0
    for line in lines:
       line = line.strip()
       if line.startswith('#'):
          pass
       elif line == '':
          pass
       else:
          cc += 1
    print(cc)



main()




