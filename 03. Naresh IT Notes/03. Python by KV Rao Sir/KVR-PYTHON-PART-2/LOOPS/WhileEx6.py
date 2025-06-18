#Program for Generating  Odd numbers within n  in reverse Order where n is +ve
#WhileEx6.py
n=int(input("Enter a Number in which we generate Odd Numbers:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("=" * 50)
    print("Odd Numbers within:{}".format(n))
    print("=" * 50)
    i=n-1 if n%2==0 else n # Ternary Operator
    while(i>=1):
        print("\t{}".format(i))
        i=i-2
    else:
        print("=" * 50)


