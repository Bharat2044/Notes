#InhProg4.py
class Circle:
    def carea(self):
        self.r=float(input("Enter Radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle=",self.ac)
class Square:
    def sarea(self):
        self.s=float(input("Enter Side:"))
        self.sa=self.s**2
        print("Area of Square=",self.sa)
class Rect(Circle,Square):
    def rarea(self):
        self.L=float(input("Enter Length:"))
        self.B = float(input("Enter Length:"))
        self.ra=self.L*self.B
        print("Area of Rect=",self.ra)
#Main Program
r=Rect()
r.rarea()
r.sarea()
r.carea()