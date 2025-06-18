#Program for finding Sum and Avg for List of Numbers
#FunSumAvgEx4.py
def  acceptvalues():
    n=int(input("Enter How Many Values Sum and Average u want to Find:"))
    if(n<=0):
        print("U can't Find sum and Avg  ur Input is Invalid")
    else:
        lst=list() # Create empty list for storing list of values
        for i in range(1,n+1):
            value=float(input("Enter {} Value:".format(i)))
            lst.append(value)
        findsumvg(lst) # One Function can call another Function called Function Chain
def findsumvg(lst): # lst=[10.0, 2.3, 5.6, 7.8, 12.0]
    if(len(lst)==0):
        print("U can't Find sum and Avg bcoz list is empty")
    else:
        s=sum(lst)# here sum() is pre-defined function used for finding sum of Numerical values
        avg=s/len(lst)
        print("--------------------------")
        print("Sum={}".format(s))
        print("Average={}".format(avg))
        print("--------------------------")

#Main program
acceptvalues() # Function Call


