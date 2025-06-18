#Program for Generating n to 1 numbers where n is +ve
#WhileEx2.py
n=int(input("Enter How Many Numbers u want to Generate in backward Direction:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    i=n # Initlization Part
    while(i>=1):
        print("\t{}".format(i))
        i-=1 # Here -= is called Short hand -(minus) Operator
    else:
        print("i am from else part of while loop")
    print("I am out-off while loop--other statements")
print("Program execution completed")



