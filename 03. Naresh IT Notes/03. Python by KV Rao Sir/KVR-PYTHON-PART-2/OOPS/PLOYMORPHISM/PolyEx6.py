#PolyEx6.py
class Circle:
    def area(self,r): # Original Method
        self.ac = 3.14 * r ** 2
        print("Area of Circle=", self.ac)
class Square:
    def area(self,s): #Original Method
        self.sa = s ** 2
        print("Area of Square=", self.sa)
class Rect(Square,Circle):
    def area(self,l,b):#Overridden Method
        self.ra = l*b
        print("Area of Rect=", self.ra)
        super().area(float(input("Enter Side:")))
        Circle.area(self,float(input("Enter Radius:")))

#Main program
r=Rect()
r.area(float(input("Enter Length:")),float(input("Enter Breadth")))



