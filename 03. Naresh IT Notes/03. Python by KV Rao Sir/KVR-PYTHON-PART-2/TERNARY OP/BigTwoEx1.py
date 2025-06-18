#Program for Finding Biggest of Two Numbers
#BigTwoEx1.py
a=float(input("Enter First Value:")) # a=10
b=float(input("Enter Second Value:"))# b=20
big= a  if a>b else b # Python Ternary Operator
print("Big({},{})={}".format(a,b,big))