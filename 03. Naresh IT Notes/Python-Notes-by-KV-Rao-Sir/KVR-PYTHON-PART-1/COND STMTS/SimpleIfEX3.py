#Program deciding whether the value is Palindrome or Not
#SimpleIfEX3.py
n=input("Enter a Value:")
if(n.upper()==n[::-1].upper()):
    print("{} is Palidrome".format(n))
if(n.lower()!=n[::-1].lower()):
    print("{} is Not Palidrome".format(n))

