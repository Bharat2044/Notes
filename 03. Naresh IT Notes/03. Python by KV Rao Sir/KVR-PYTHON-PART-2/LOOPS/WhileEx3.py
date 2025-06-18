#Program for Generating  even numbers within n where n is +ve
#WhileEx3.py
n=int(input("Enter a Number in which we generate Even Numbers:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("=" * 50)
    print("Even Numbers within:{}".format(n))
    print("=" * 50)
    i=2
    while(i<=n):
        print("\t{}".format(i))
        i+=2
    else:
        print("="*50)

