#Program for Defining a Function for FINDING Biggest of Two Numbers
#AnonymousFunEx2.py

findbig=lambda a,b:a if a>b else b if b>a else "Both the Values are Equal" # Anonymous function definition

#Main Program
print("Enter Two Values for Finding Big:")
a,b=float(input()),float(input())
bv=findbig(a,b)
print("Big({},{})={}".format(a,b,bv))
