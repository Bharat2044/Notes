#Program for finding Sum and Avg for List of Numbers
#FunSumAvgEx4.py
def  acceptvalues():
    n=int(input("Enter How Many Values Sum and Average u want to Find:"))
    if(n<=0):
        return list()
    else:
        lst=list() # Create empty list for storing list of values
        for i in range(1,n+1):
            value=float(input("Enter {} Value:".format(i)))
            lst.append(value)
        return lst # One Function can call another Function called Function Chain
def findsumavg(): # lst=[10.0, 2.3, 5.6, 7.8, 12.0]
    kvr=acceptvalues()
    res="Empty List" if len(kvr)==0 else cal(kvr)
    print(res)
def cal(lst):
    s=sum(lst)
    av=s/len(lst)
    return "Sum="+str(s)+"\nAvg="+str(av)
#Main program
findsumavg() # Function Call


