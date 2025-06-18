#Program for deciding whether the given number is +VE or -VE or Zero
#IfElseEx1.py
n=float(input("Enter a Number:")) # n=10
if(n>0):
    print("{} is +VE".format(n))
else:
    if(n<0):
        print("{} is -VE".format(n))
    else:
        print("{} is ZERO".format(n))
print("Program Execution Completed")