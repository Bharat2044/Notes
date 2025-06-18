#Program for Deciding whether It is +Ve or -VE Or zero
#PosNegZeroEx.py
n=float(input("Enter any Numerical Value:")) # n= 0
res="+VE" if n>0 else "-VE" if n<0 else "ZERO"
print("{} is {}".format(n,res))
