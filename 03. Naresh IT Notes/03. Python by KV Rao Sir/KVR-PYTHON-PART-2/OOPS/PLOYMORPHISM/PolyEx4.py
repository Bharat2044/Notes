#PolyEx4.py
class Circle:
    def __init__(self): # Original Constructor
        self.r = float(input("Enter Radius:"))
        self.ac = 3.14 * self.r ** 2
        print("Area of Circle=", self.ac)
class Square(Circle):
    def __init__(self):# Overridden Constructor
        self.s = float(input("Enter Side:"))
        self.sa = self.s ** 2
        print("Area of Square=", self.sa)
class Rect(Square):
    def __init__(self):# Overridden Constructor
        self.L = float(input("Enter Length:"))
        self.B = float(input("Enter Breadth:"))
        self.ra = self.L * self.B
        print("Area of Rect=", self.ra)
        Circle.__init__(self)
        Square.__init__(self)

#main Program
r=Rect()# Object Creation


