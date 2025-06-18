#Program for generating Random Mul Tables
#InnerLoopEx7.py
n=int(input("Enter How Many Random Mul Tables u want:"))#n=5
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    lst=[] # OR lst=list() ---creating empty list for adding the values
    for i in range(1,n+1):
        value=int(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("=" * 50)
        print("List of Values:{}".format(lst)) # [19, 17, 9, -4, 16]
        print("=" * 50)
        #Logic for Mul Table for List of Random values
        for num in lst: # outer Loop
            if(num<=0):
                print("{} is Invalid Number:".format(num))
                continue
            print("Mul Table for :{}".format(num))
            print("--------------------------------")
            for i in range(1,11):
                print("\t{} x {}={}".format(num,i,num*i))
            else:
                print("--------------------------------")


