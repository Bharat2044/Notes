#Program for accepting list of Value and Obtains Squares
#MapEx1.py
def squares(value):
    return value**2

#Main Program
print("Enter List of Values separated by space:")
lst=[ float(val) for val in input().split() if val.isdigit()]
mapobj=map(squares,lst)
print("Type of sqlist=",type(mapobj))
#Convert Map Object into List
sqlist=list(mapobj)
print("Given List=",lst)
print("Square List=",sqlist)
