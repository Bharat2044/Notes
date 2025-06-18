#Program for accepting numerical integer value and decide whether it is prime or not
#BreakStmtEx5.py
n=int(input("Enter a Number:"))#n=5
if(n<=1):
    print("{} is invalid Input".format(n))
else:
    res="PRIME"
    for i in range(2,n):
        if(n%i==0):
            res="NOT PRIME"
            break
    print("{} is {}".format(n,res))
