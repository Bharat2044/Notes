#Program for Reading lst of Values and also Squares of those numbers by using Comprehension concept
#SetCompEx1.py
print("Enter list of  Values for finding their squares Separated by space:")
d={float(value):float(value)**2   for value in input().split() }  # Dict Comprehension
print(d,type(d))
print("---------------------------------------------")
for k,v in d.items():
    print("\t{}--->{}".format(k,v))
