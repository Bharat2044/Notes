#InnerLoopEx1.py--for loop in for loop
for i in range(1,6):#Outer Loop
    print("Outer loop: Value of i=",i)
    print("------------------------------")
    for j in range(1,4):#Inner loop
        print("\tInner loop:",j)
    else:
        print("Outoff Inner Loop")
        print("------------------------------")
else:
    print("Outoff outer loop")
