#Program for Reading List of Values and Obtains +ve Values
#FilterEx6.py
print("Enter List of Values Separated By Comma:")
lst=[float(val) for val in input().split(",")] # lst=[10,-23,34.56,-5.6,23,-45]
print("Given List of Values=",lst)
posvals=list(filter(lambda n: n>0 , lst))
print("List of +VE Values=",posvals)

