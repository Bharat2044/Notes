#Program Obtaining List of Primes within the range
#InnerLoopEx5.py
n=int(input("Enter the Range in which prime Numbers u want display:"))
if(n<=1):
    print("{} is Invalid input".format(n))
else:
    print("List of Primes within:{}".format(n))
    for num in range(2,n+1): # Outer loop --Supply the Value to Inner loop
        res=True
        for i in range(2,num):# Inner loop--Decides whether num is prime or not
            if(num%i==0):
                res=False
                break
        if(res):
            print("\t\t",num)
