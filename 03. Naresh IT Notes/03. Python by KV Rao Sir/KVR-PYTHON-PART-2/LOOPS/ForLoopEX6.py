#Program for Generating  Multiplication table for  n where n is +ve
#ForLoopEX6.py
n=int(input("Enter a Number in which we generate Mul table:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("-----------------------------------------")
    print("Mul Table for :{}".format(n))
    print("-----------------------------------------")
    for i in range(1,11):
        print("\t{} x {} = {}".format(n,i,n*i))
    else:
        print("-----------------------------------------")
