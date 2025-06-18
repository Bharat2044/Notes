#PolyEx2.py
class Circle:
    def __init__(self,r): # Original Method
        self.ac = 3.14 * r ** 2
        print("Area of Circle=", self.ac)
class Square:
    def __init__(self,s): #Original Method
        self.sa = s ** 2
        print("Area of Square=", self.sa)
class Rect(Square,Circle):
    def __init__(self,l,b):#Overridden Method
        self.ra = l*b
        print("Area of Rect=", self.ra)
        super().__init__(float(input("Enter Side:")))
        Circle.__init__(self,float(input("Enter Radius:")))

#Main program
r=Rect(float(input("Enter Length:")),float(input("Enter Breadth:")))




