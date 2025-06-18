#Program for finding Factorial of a number
#FactEx2.py
num=int(input("Enter a Number for Cal Factorial:"))
if(num<0):
    print("{} is Invalid input".format(num))
else:
    #num=4---> 4 x 3 x 2 x 1
    fact=1 # multiplicative Identity
    tnum=num #Preserve the num value in tnum
    while(num>0):
        fact*=num
        num-=1
    else:
        print("Fact({})={}".format(tnum,fact))


