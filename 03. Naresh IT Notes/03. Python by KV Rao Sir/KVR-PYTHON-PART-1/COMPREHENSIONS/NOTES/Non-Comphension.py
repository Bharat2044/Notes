#Program for Reading the Values from Keyboard
n=int(input("Enter How Many values u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        value=float(input("Enter {} Value:".format(i)))
        lst.append(value)
    print("content of list=",lst)
