#Program for finding sum of digits of Given Number
#DigitsSumEx3.py---
num=input("Enter a Number:")
print("Given Number=",num)#num=2367
s=0
i=0
while(i<len(num)):
    s=s+float(num[i])
    i=i+1
else:
    print("sum of digits=", s)