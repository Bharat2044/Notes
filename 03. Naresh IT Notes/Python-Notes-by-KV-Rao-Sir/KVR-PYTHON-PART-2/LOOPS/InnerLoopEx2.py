#InnerLoopEx2.py--while loop in while loop
i=1
while(i<6): # Outer Loop
    print("Outer loop: Value of i=", i)
    print("------------------------------")
    j=1
    while(j<=3): # Inner loop
        print("\tInner loop:", j)
        j+=1
    else:
        i+=1
        print("Outoff Inner Loop")
        print("------------------------------")
else:
    print("Outoff outer loop")
