#Program for Reading tuple of Values by using Comprehension concept
#TupleCompEx1.py
print("Enter tuple of Values Separated by Space:")
t=list(float(value)  for value in input().split()) # list Comprehension
print(t,type(t)) # Here t is an object of <class 'generator'>
#Convert generator object into tuple type
tpl=list(t)
print(tpl,type(tpl))
