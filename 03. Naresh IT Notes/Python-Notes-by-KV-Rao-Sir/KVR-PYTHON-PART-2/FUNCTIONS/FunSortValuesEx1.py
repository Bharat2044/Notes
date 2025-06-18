#Program for accepting list of values and sort then in Both Ascending and Decending
#FunSortValuesEx1.py
def  getvalues(op):
    print("Enter List of Value for  '{}'(Press @ to stop):".format(op))
    lst=[]
    while(True):
        value=input()
        if(value=="@"):
            break
        lst.append(float(value))
    return lst
def sortdata():
    lst=getvalues("Sorting")
    if(len(lst)==0):
        print("List if empty-sorting not possible")
    else:
        #Code of getting list of vals in ASCENDING ORDER
        lst.sort()
        print("ASCENDING ORDER={}".format(lst))
        lst.sort(reverse=True)
        print("DESCENDING ORDER={}".format(lst))
#Main program
sortdata()
