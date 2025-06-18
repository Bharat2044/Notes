#InnerLoopEx3.py--for loop in while loop
i=1
while(i<6): # Outer Loop
    print("Outer loop: Value of i=", i)
    print("------------------------------")
    for j in range(3,0,-1): # Inner loop
        print("\tInner loop:", j)
    else:
        i+=1
        print("Outoff Inner Loop")
        print("------------------------------")
else:
    print("Outoff outer loop")