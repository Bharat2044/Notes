#Program for Defining a Function for cal addition of Two Numbers
#AnonymousFunEx2.py
addop=lambda a,b : a+b # Anonymous Function Definition

#Main program
print("Enter Two Values:")
a,b=float(input()),float(input())
c=addop(a,b)
print("sum({},{})={}".format(a,b,c))
print("---------------OR---------------------")
print("{} + {} = {}".format(a,b,addop(a,b)))