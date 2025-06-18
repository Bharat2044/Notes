#Program for accepting list of Value and Obtains Squares
#MapEx2.py
squares=lambda value: value**2
#Main Program
print("Enter List of Values separated by space:")
lst=[ float(val) for val in input().split() if val.isdigit()]
sqlist=tuple(map(squares,lst))
sqrtlist=list(map(lambda value:round(value**0.5,2),lst))
print("----------------------------------")
print("Given List=",lst)
print("Square List=",sqlist)
print("Square Root List=",sqrtlist)
print("----------------------------------")