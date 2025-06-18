#Program for Reading List of Values by using Comprehension concept
#ListCompEx1.py
print("Enter List  of Values Separated by Space:")
lst=[ float(value)  for value in input().split()]  # list Comprehension
print(lst,type(lst))