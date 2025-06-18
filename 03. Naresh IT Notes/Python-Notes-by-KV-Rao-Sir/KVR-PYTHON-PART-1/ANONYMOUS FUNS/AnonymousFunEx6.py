#Program for Defining a Function for FINDING Max and Min from List of Numbers
#AnonymousFunEx6.py

maxv=lambda lst: max(lst)  # Anonymous Function
minv=lambda lstobj: min(lst) # Anonymous Function


#Main Program
print("Enter List of Values Separated by Space:")

lst=[float(val) for val in input().split()]
if(len(lst)==0):
	print("List is empty -can't find Max and Min")
elif(len(lst)==1):
	print("List Contains Single Value Max and Min={}".format(lst[0]))
elif(len(set(lst))==1):
	print("List Contains Same Values--all are equal")
else:
	mv1=maxv(lst)
	mv2=minv(lst)
	print("Max({})={}".format(lst,mv1))
	print("Min({})={}".format(lst,mv2))