#Program for Reading set of Values by using Comprehension concept
#SetCompEx1.py
print("Enter Set of  Values Separated by Comma:")
st={ float(value)  for value in input().split(",")} #  set Comprehension
print(st,type(st))