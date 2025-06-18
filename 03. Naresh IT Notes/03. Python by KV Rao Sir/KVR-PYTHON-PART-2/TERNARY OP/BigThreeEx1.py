#Program for Deciding Biggest of Three Numbers and Checks for Equality
#BigThreeEx1.py
print("Enter Three Values")
a,b,c=float(input()),float(input()),float(input())
#Logic for biggest of Three Nos.
bv=a if (a>=b) and (a>c) else b if (b>a) and (b>=c) else c if (c>=a) and (c>b) else "ALL VALUES ARE EQUAL"
print("Big({},{},{})={}".format(a,b,c,bv))
