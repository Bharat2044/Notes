#Program for Defining a Function for cal addition of Two Numbers
#AnonymousFunEx1.py
def   sumop(a,b): # Normal Function Definitiion
     c=a+b
     return c

addop=lambda a,b : a+b # Anonymous Function Definition

#Main program
print("Type of sumop=",type(sumop)) # Type of sumop= <class 'function'>
#Here sumop is an object of <class, function> and It can be used for as function call
res=sumop(10,20) # Normal Function Call
print("Sum =",res)
print("========================================")
print("Type of addop=",type(addop)) # Type of addop= <class 'function'>
#Here addop is an object of <class, function> and It can be used for as function call
res1=addop(100,200) # Anonymous Function Call
print("Sum=",res1)