#InhProg1.py
class C1:
    def getA(self):
        self.a=100
class C2(C1):
    def getB(self):
        self.b=200
    def addop(self):
        self.c=self.a+self.b
        print("Sum({},{})={}".format(self.a,self.b,self.c))
#Main Program
o2=C2()
print(o2.__dict__)
o2.getB()
print(o2.__dict__)
o2.getA()
print(o2.__dict__)
o2.addop()

