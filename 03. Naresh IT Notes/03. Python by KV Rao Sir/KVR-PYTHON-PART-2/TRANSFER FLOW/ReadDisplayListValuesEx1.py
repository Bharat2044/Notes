#Read n values and place them in list and display the values
#ReadDisplayListValuesEx1.py
n=int(input("Enter How Many Numbers u want:"))#n=5
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    lst=[] # OR lst=list() ---creating empty list for adding the values
    for i in range(1,n+1):
        value=float(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("=" * 50)
        print("List of Values:{}".format(lst))
        print("=" * 50)


