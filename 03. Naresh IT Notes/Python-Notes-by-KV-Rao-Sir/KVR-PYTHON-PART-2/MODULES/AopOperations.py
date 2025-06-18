#AopOperations.py<---File Name and Module Name
def addop():
    print("Enter Two Values for Addition:")
    a,b=float(input()),float(input())
    print("sum({},{})={}".format(a,b,a+b))
def subop():
    print("Enter Two Values for Substraction:")
    a, b = float(input()), float(input())
    print("sub({},{})={}".format(a, b, a - b))
def mulop():
    print("Enter Two Values for Multiplication:")
    a, b = float(input()), float(input())
    print("Mul({},{})={}".format(a, b, a * b))
def divop():
    print("Enter Two Values for Division:")
    a, b = float(input()), float(input())
    print("NormalDiv({},{})={}".format(a, b, a/ b))
    print("FloorDiv({},{})={}".format(a, b, a // b))
def modop():
    print("Enter Two Values for Modulo Div:")
    a, b = float(input()), float(input())
    print("Mod({},{})={}".format(a, b, a % b))
def expop():
    a, b = float(input("Enter Base:")), float(input("Enter Power:"))
    print("Pow({},{})={}".format(a, b, a ** b))
