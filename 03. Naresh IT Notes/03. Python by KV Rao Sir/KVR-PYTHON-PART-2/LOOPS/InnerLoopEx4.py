#InnerLoopEx4.py--while loop in for loop
for i in range(5,0,-1):#Outer Loop
    print("Outer loop: Value of i=",i)
    print("------------------------------")
    j=3
    while(j>=1):#Inner loop
        print("\tInner loop:",j)
        j-=1
    else:
        print("Outoff Inner Loop")
        print("------------------------------")
else:
    print("Outoff outer loop")