#Program for finding sum of digits of Given Number
#DigitsSumEx1.py---
num=int(input("Enter a Number:"))
print("Given Number=",num)#num=2367
s=0
while(num>0):
    r=num%10
    s=s+r # OR s+=r
    num=num//10
else:
    print("sum of digits=",s)


