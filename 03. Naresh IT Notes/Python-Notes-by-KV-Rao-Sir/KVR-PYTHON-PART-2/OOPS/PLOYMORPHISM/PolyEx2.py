#PolyEx2.py
class Circle:
    def area(self): # Original Method
        self.r = float(input("Enter Radius:"))
        self.ac = 3.14 * self.r ** 2
        print("Area of Circle=", self.ac)
class Square:
    def area(self): #Original Method
        self.s = float(input("Enter Side:"))
        self.sa = self.s ** 2
        print("Area of Square=", self.sa)
class Rect(Square,Circle):
    def area(self):#Overridden Method
        self.L = float(input("Enter Length:"))
        self.B = float(input("Enter Length:"))
        self.ra = self.L * self.B
        print("Area of Rect=", self.ra)
        super().area()
        Circle.area(self)

#Main program
r=Rect()
r.area()



