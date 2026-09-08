import sys
from pyfiglet import Figlet
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        x = input("Input: ")
        figlet.setFont(font=random.choice(fonts))
        print(f"Output: {figlet.renderText(x)}")
    elif (len(sys.argv) == 3) and (sys.argv[2] in fonts):
        if ((sys.argv[1] ==  "-f" ) or (sys.argv[1] == "--font")):
            figlet.setFont(font=sys.argv[2])
            x = input("Input: ")
            print(f"Output: {figlet.renderText(x)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")




if __name__ == "__main__":
    main()
