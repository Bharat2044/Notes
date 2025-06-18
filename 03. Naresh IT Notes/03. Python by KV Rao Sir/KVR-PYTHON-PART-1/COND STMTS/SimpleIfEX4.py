#Program deciding whether the value is Palindrome or Not
#SimpleIfEX3.py
n=input("Enter a Value:").upper()
if(n==n[::-1]):
    print("{} is Palidrome".format(n))
if(n!=n[::-1]):
    print("{} is Not Palidrome".format(n))

