from PIL import Image,ImageOps
import os
import sys

def check_args():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    before_name = sys.argv[1]
    after_name = sys.argv[2]

    extension_before = os.path.splitext(before_name)[1]
    extension_after = os.path.splitext(after_name)[1]

    if extension_before != ".jpg" and extension_before != ".jpeg" and extension_before != ".png":
        sys.exit("Invalid output")

    if extension_before != extension_after:
        sys.exit("Input and output have different extensions")

    if not os.path.exists(before_name):
        sys.exit("Input does not exist")

def main():
    check_args()

    shirt = Image.open("shirt.png")
    before = Image.open(sys.argv[1])
    before = ImageOps.fit(before, shirt.size)
    before.paste(shirt, (0, 0), shirt)
    before.save(sys.argv[2])    

if __name__ == "__main__":
    main()