import sys
import os
from PIL import Image, ImageOps

def main():
    # 1. Check count
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # 2. Get extensions and verify validity
    valid_extensions = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()

    if ext1 not in valid_extensions:
        sys.exit("Invalid input")
    if ext2 not in valid_extensions:
        sys.exit("Invalid output")

    # 3. Check if extensions match
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    f = sys.argv[1]
    t = sys.argv[2]

    # Image Processing 
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size

        with Image.open(f) as im:
            k = ImageOps.fit(im, size)
            k.paste(shirt, shirt) # Using shirt as mask for transparency
            k.save(t)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
