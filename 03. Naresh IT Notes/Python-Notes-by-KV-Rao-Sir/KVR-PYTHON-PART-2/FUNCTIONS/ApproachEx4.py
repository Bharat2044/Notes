#Function for Adding Two Numbers
#ApproachEx4.py
# INPUT: Taken Inside of Function Body
# PROCEES:Done Inside of Function Body
# RESULT: Gives to Function call
def addop():
    # Input
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    # Process
    c=a+b
    #gives the result back to function call
    return a,b,c # here return stmt can return Either One Value or More Values
#Main Program
a,b,res=addop()#Function call with Multi Line assigment
print("sum({},{})={}".format(a,b,res))
print("===========OR================")
res=addop() # Function call with Single Line assigment
# Here res is of type <class, 'tuple'>
print("sum({},{})={}".format(res[0],res[1],res[2]))
