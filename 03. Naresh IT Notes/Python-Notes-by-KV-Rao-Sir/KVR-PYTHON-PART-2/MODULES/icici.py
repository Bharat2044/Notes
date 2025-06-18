#icici.py<---File Name and Module name
bname="ICICI"
addr="HYD" # here bname and addr are called Global Variables
def simpleint():
    p=float(input("Enter Principle Amount:"))
    t = float(input("Enter Time:"))
    r = float(input("Enter Rate of Interest:"))
    #Cal si
    si=(p*t*r)/100
    totamt=p+si
    print("-------------------------------------")
    print("Principle Amount:",p)
    print("Time:",t)
    print("Rate of Interest:",r)
    print("Simple Interest=",si)
    print("Total Amount to pay:",totamt)
    print("-------------------------------------")