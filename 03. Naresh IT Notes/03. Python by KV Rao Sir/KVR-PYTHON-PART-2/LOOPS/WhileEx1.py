#Program for Generating 1 to n numbers where n is +ve
#WhileEx1.py
n=int(input("Enter How Many Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    i=1 # Initlization Part
    while(i<=n): # Cond Part
        print("\t{}".format(i))
        i=i+1  # Updation Part--Incr
    print("Other statements in while loop")
print("Program Execution Completed")