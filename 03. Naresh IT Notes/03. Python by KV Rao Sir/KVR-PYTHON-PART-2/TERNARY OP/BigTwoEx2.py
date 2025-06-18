#Program for Finding Biggest of Two Numbers  and Check for Equality
#BigTwoEx2.py
a=float(input("Enter First Value:")) # a=10
b=float(input("Enter Second Value:"))# b=10
res= a if a>b else b if b>a else "Both Values are Equal"
print("Big({},{})={}".format(a,b,res))
