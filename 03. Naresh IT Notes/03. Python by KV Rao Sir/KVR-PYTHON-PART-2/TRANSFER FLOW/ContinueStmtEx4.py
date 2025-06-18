#ContinueStmtEx4.py
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
        print("List of Values:{}".format(lst))#[100.0, -200.0, 45.0, -56.0, 0.0]
        print("=" * 50)
        #get +Ve Values and place them list
        pslist=[]
        for value in lst:
            if(value<=0):
                continue
            pslist.append(value)
        else:
            print("------------------------------------------")
            print("List of +Ve Values:{}".format(pslist))
            print("Number of +Ve Values={}".format(len(pslist)))
            print("------------------------------------------")
            # get -Ve Values and place them list
            nglist=list()
            for value in lst:
                if(value>=0):pass
                else:
                    nglist.append(value)
            else:
                print("List of -Ve Values:{}".format(nglist))
                print("Number of -Ve Values={}".format(len(nglist)))
                print("------------------------------------------")





