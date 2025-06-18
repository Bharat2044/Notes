#Program for Swapping of Two  Inetger Values Only
#AssignmentOperatorEx3.py
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:")) # Multi Line assignment
print("*"*50)
print("Original Value of a={}".format(a))
print("Original Value of b={}".format(b))
print("*"*50)
#swapping OR Interchanging logic
a=a+b
b=a-b
a=a-b
print("Swapped Value of a={}".format(a))
print("Swapped Value of b={}".format(b))
print("*"*50)