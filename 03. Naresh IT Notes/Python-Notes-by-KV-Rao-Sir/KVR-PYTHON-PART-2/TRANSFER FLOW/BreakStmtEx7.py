#Program for accepting numerical integer value and decide whether it is prime or not
#BreakStmtEx7.py
n=int(input("Enter a Number:"))#n=5
if(n<=1):
    print("{} is invalid Input".format(n))
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break
    print("{} is {}".format(n,"PRIME" if res else "NOT PRIME"))
