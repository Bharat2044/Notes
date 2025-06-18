#Program for generating Mul Tables from 1 to n
#InnerLoopEx6.py
n=int(input("Enter How Many Mul Tables u want:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    for num in range(1,n+1):# Outer for loop --supply the number
        print("*"*50)
        print("Mul Table for :{}".format(num))
        print("*" * 50)
        for i in range(1,11): # Inner for loop--generate mul table
            print("\t{} x {}={}".format(num,i,num*i))
        else:
            print("*" * 50)
