#Program for Defining a Function for FINDING Biggest of Three Numbers
#AnonymousFunEx5.py

findbig=lambda a,b,c: a if (b<=a>c) else b if a<b>=c else c if (a<=c>b) else "All Values are equal"  #  Anonymous Function Definition
findsmall=lambda a,b,c: a if (b>=a<c) else b if (a>b<=c) else c if (a>=c<b) else "All Values are equal"  #  Anonymous Function Definition
#Main Program
print("Enter Three Values for Finding Big:")
a,b,c=float(input()),float(input()),float(input())
bv=findbig(a,b,c)
sv=findsmall(a,b,c)
print("Big({},{},{})={}".format(a,b,c,bv))
print("Small({},{},{})={}".format(a,b,c,sv))
