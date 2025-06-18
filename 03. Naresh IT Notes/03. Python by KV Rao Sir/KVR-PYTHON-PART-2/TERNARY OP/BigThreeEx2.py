#Program for Deciding Biggest of Three Numbers and Checks for Equality
#BigThreeEx2.py
print("Enter Three Values")
a,b,c=float(input()),float(input()),float(input())
#Logic for biggest of Three Nos.
bv=a if b<=a>c  else b if a<b>=c else c if a<=c>b else "ALL VALUES ARE EQUAL"
print("Big({},{},{})={}".format(a,b,c,bv))
