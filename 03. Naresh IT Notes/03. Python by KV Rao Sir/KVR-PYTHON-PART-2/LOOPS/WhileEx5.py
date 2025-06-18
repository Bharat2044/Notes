#Program for Generating  Odd numbers within n where n is +ve
#WhileEx5.py
n=int(input("Enter a Number in which we generate Odd Numbers:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("=" * 50)
    print("Odd Numbers within:{}".format(n))
    print("=" * 50)
    i=1
    while(i<=n):
        print("\t{}".format(i))
        i+=2
    else:
        print("="*50)