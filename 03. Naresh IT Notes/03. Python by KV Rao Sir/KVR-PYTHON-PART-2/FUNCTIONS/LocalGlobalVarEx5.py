#LocalGlobalVarEx5.py
def  addop(a,b):
	print("Inside of addop()")
	print(a,b)
	print(x,y)
	c=a+b
	return c
def  acceess():
	print("Acsess()---Sum=",z)
#Main program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
z=addop(x,y) # Function Call
print("Main Program=",z)
acceess() # For this Function Call, z is called global variables
