#Program for Reading List of Values and Obtains +ve Values
#FilterEx5.py
pos=lambda value: value>0
#Main Program
print("Enter List of Values Separated By Comma:")
lst=[float(val) for val in input().split(",")] # lst=[10,-23,34.56,-5.6,23,-45]
print("Given List of Values=",lst)
posvals=list(filter(pos,lst))
print("List of +VE Values=",posvals)

