#MatchCaseEX1.py
print("*"*50)
print("Arithmetic Operations")
print("*"*50)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Mod Div")
print("\t6.Exponentiation")
print("\t7.Exit")
print("*"*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1:
        print("Enter Two Values for Addition")
        a,b=float(input()),float(input())
        print("sum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Substraction")
        a, b = float(input()), float(input())
        print("sub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two Values for Multiplication")
        a, b = float(input()), float(input())
        print("Mul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two Values for Division")
        a, b = float(input()), float(input())
        print("NormalDiv({},{})={}".format(a, b, a / b))
        print("FloorDiv({},{})={}".format(a, b, a // b))
    case 5:
            print("Enter Two Values for Mod Div")
            a, b = float(input()), float(input())
            print("ModDIV({},{})={}".format(a, b, a% b))
    case 6:
            a, b = float(input("Enter Base:")), float(input("Enter Exp:"))
            print("Pow({},{})={}".format(a, b, a ** b))
    case 7:
        print("Thx for using program")
    case _:  # Default Case Block
        print("Ur Selection of Operation is wrong-try again")
        
print("Program Execution Completed!!!!")


