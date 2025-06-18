#Function for Adding Two Numbers
#ApproachEx1.py
# INPUT: Taken from Function call
# PROCEES: Done Inside of Function Body
# RESULT: Gives to Function call
def  addop(a,b): # Here a,b are called Formal Parameters
    c=a+b # Here c is called Local Variable
    return c
#Main program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
z=addop(x,y) # Function Call
print("sum({},{})={}".format(x,y,z))
print("-------------------------------------")
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=addop(a,b) # Function Call
print("sum({},{})={}".format(a,b,c))
