#Program for cal simple interest and cal total amount to pay
#ArithOperatorsEx2.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#Cal si and totamt
si=(p*t*r)/100
totamt=p+si
#display the result
print("*"*40)
print("\tResults of Simple Interest")
print("*"*40)
print("\t\t Principle Amount:{} ".format(p))
print("\t\t Time:{} ".format(t))
print("\t\t Rate of Interest: {}".format(r))
print("\t\tSIMPLE INTEREST:{}".format(si))
print("\t\tTOTAL AMOUN TO PAY:{}".format(totamt))
print("+"*40)
