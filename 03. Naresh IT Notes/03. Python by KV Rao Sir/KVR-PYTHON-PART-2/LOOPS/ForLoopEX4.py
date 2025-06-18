#Program for Generating 1 to n numbers where n is +ve
#ForLoopEx4.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-------------------------------------")
    print("Numbers within :{}".format(n))
    print("-------------------------------------")
    for i in range(1,n+1):
        print("\t{}".format(i))
    else:
        print("-------------------------------------")