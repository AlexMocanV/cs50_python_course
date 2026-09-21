import pyfiglet
import sys
import random

available_fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    x = input("Input: ")
    print(pyfiglet.figlet_format(x, font = random.choice(available_fonts)))
elif len(sys.argv) == 3 and (sys.argv[2] in available_fonts) and (sys.argv[1] in  ["-f", "--font"]):
    x = input("Input: ")
    print(pyfiglet.figlet_format(x, font = sys.argv[2])) 
else:
    sys.exit("wrong format")
        