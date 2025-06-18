#Program for finding max and min from List of Values
#Don't use max() and min()
#FindMaxMinEx1.py
def  getvalues(op):
    print("Enter List of Value for Finding '{}'(Press @ to stop):".format(op))
    lst=[]
    while(True):
        value=input()
        if(value=="@"):
            break
        lst.append(float(value))
    return lst
def findmax(): # [10.0, 20.0, -3.0, 30.0, 15.0, 16.0]  OR []
    lst=getvalues("MAX")
    if(len(lst)==0):
        print("List is empty can't find max")
    else:
        mv=lst[0] # 20
        for i in range(1,len(lst)):
            if(lst[i]>mv):
                mv=lst[i]
        print("Max({})={}".format(lst,mv))

def findmin():
    lst=getvalues("MIN")
    if (len(lst) == 0):
        print("List is empty can't find min")
    else:
        mv = lst[0]  # 20
        for val in lst:
            if(val<mv):
                mv=val
        print("Min({})={}".format(lst, mv))

#Main Program
findmax()
findmin()