import sys
from PIL import Image, ImageOps

def main():
    c = []

    #Command Line Argument
    if len(sys.argv) !=3:
        sys.exit("Too many/few arguments!")
    elif not sys.argv[1].endswith('.png') or not sys.argv[2].endswith('.png'):
        sys.exit("Does not end with '.py'")
    elif not sys.argv[1].endswith('.jpg') or not sys.argv[2].endswith('.jpg'):
        sys.exit("Does not end with '.py'")
    elif sys.argv[1].endswith('.jpg') and sys.argv[2].endswith('.png'):
        sys.exit("Input and output have diferent extensions")
    elif sys.argv[1].endswith('.png') and sys.argv[2].endswith('.jpg'):
        sys.exit("Input and output have diferent extensions")
    else:
        f = sys.argv[1]
        t = sys.argv[2]

    #Open shirt.png
    shirt = Image.open("shirt.png")
    #Save shirt height& width as tuple
    size = shirt.size

    #Open input
    with Image.open(f) as im:
        #Resize and crop input w/ ImageOps.fit
        k = ImageOps.fit(im, size)
        #using default values for method, bleed, and centering, overlay the shirt with Image.paste
        k.paste(shirt, shirt)
        #save the result with Image.save
        k.save(t)

main()
