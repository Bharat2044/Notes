#Program for adding of two Numbrs by using Classes and Objects
class SumOp:
    def getvals(self):
        self.a=float(input("Enter First value:"))
        self.b=float(input("Enter Second Value:"))
    def calculate(self):
        self.c=self.a+self.b
    def dispvals(self):
        print("sum({},{})={}".format(self.a,self.b,self.c))

#Main Program
so=SumOp()
so.getvals()
so.calculate()
so.dispvals()