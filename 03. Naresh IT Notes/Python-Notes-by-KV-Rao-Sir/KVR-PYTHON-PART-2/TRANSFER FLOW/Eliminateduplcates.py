#Eliminateduplcates.py
value=input("Enter Ur Value(Num OR Non-Num:") #value="MISSISSIPPI
lst=list()
for val in value:
    if(val in lst):pass
    else:
        lst.append(val)
else:
    print("Unique Values")
    for val in lst:
        print(val,end="")

