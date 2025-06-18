#Function for Adding Two Numbers
#ApproachEx3.py
# INPUT: Taken from Function call
# PROCEES: Done Inside of Function Body
# RESULT: Displayed in Function Body
def  addop(k,v):
    r=k+v # Here 'r' is called Local Variable
    print("Sum({},{})={}".format(k,v,r))

#Main Program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
addop(x,y) # Function call

