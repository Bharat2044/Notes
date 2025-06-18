#Program for finding Factorial of a number
#FactEx1.py
num=int(input("Enter a Number for Cal Factorial:"))
if(num<0):
    print("{} is Invalid input".format(num))
else:
    #num=4---> 4 x 3 x 2 x 1
    fact=1 # multiplicative Identity
    for i in range(num,0,-1):
        fact*=i
    else:
        print("Fact({})={}".format(num,fact))


