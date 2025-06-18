#FigureDemo.py<---Main program
from FigureMenu import figmenu
from Circle import area as ca
from Rect import area as ra
from Square import area as sa
from Triangle import area as ta
import sys
while(True):
    figmenu()
    ch=int(input("Enter Choice:"))
    match(ch):
        case 1:
            ra()
        case 2:
            sa()
        case 3:
            ca()
        case 4:
            ta()
        case 5:
            print("Thx for using Program")
            sys.exit()
        case _:
            print("Ur Selection of Operation is wrong--try again")