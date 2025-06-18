#Function for addition of two Numbers
def addop(a,b): # Here a, b are called Formal Parameters
    print("I am inside of Function Def")
    c=a+b # Here c is called Local Variable
    return c # Here return is kwd used for returning the local variable value to the Other part of progran
#Main Program
print("I am after function definition")
print("Type of addop=",type(addop)) # <class 'function'>
res=addop(10,20) # Function call
print("sum=",res)
print("----------------------------")
res=addop(100,200) # Function call
print("Sum=",res)

