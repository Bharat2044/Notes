#Program for Defining a Function for FINDING Max and Min from List of Numbers
#AnonymousFunEx7.py
def NITmax(lst):
	if(len(lst)==0):
		return "List is Empty--Can't Find Max and Min"
	elif(len(set(lst))==1):
		return("List Contains Single Value Max and Min={}".format(lst[0]))
	else:
		maxv=lst[0]  # lst=[10,20,15,34,6,7]
		for val in lst:
			if(val>maxv):
				maxv=val
		return maxv

def NITmin(lst):
	if(len(lst)==0):
		return "List is Empty--Can't Find Max and Min"
	elif(len(set(lst))==1):
		return("List Contains Single Value Max and Min={}".format(lst[0]))
	else:
		minv=lst[0]  # lst=[10,20,15,34,6,7]
		for val in lst:
			if(val<minv):
				minv=val
		return minv


mxv=lambda lst: NITmax(lst)  # Anonymous Function
mnv=lambda lstobj: NITmin(lst) # Anonymous Function


#Main Program
print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()]
b=mxv(lst)
s=mnv(lst)
print("Max({})={}".format(lst,b))
print("Min({})={}".format(lst,s))