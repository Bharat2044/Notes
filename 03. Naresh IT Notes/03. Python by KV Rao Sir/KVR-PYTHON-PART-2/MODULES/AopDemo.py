#AopDemo.py<--Main Program
from AopMenu import menu
from AopOperations import addop,subop,mulop,divop,expop,modop
import sys
while(True):
    menu()
    ch=int(input("Enter Ur Choice:"))
    match(ch):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            modop()
        case 6:
            expop()
        case 7:
            print("Thx for using program")
            sys.exit()
        case _:
            print("Ur Selection of Operation is wrong-try again")