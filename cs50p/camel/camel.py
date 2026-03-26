import re
x = input("camelCase: ")
for _ in x:
    if _ .isupper():
        #first, add an Underscore
        x = re.sub(r'[A-Z]',  r'_\g<0>', x)
        #second, convert to lower
        x = x.lower()
print(x)
