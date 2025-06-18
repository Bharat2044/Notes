#Program for Accepting List Values and Filter Only Numerical Integer Values.
#FilterEx1.py
def getintvalues(value): # Normal Function Definition
    if(value[0]=="-") and (value[1:].isdigit()):
            return True
    elif(value.isdigit()):
        return True
    else:
        return False
#Main Program
print("Enter List of Values separated by space:")
lst=[val for val in input().split()]#['10', 'Rossum', '34', 'True', '2+3j', '34.56']
print("Content of lst=",lst)
vals=filter(getintvalues,lst)
print("Type of vals=",type(vals))
#Convert filter object into list
intvals=list(vals)
print("List of Integers=",intvals)