#Program for Generating 1 to n numbers  in reversed order where n is +ve
#ForLoopEx4.py
n=int(input("Enter How Many Numbers u want to generate in reverse Order:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-------------------------------------")
    print("Numbers in Reversed Order within :{}".format(n))
    print("-------------------------------------")
    for i in range(n,0,-1):
        print("\t{}".format(i))
    else:
        print("-------------------------------------")