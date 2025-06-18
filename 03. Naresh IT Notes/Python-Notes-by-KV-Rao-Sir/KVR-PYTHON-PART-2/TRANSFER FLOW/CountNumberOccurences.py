#CountNumberOccurences.py
value=input("Enter Ur Value(Num OR Non-Num:") #value="MISSISSIPPI
d=dict()
for val in value:
    if val not in d:
        d[val]=1
    else:
        d[val]=d[val]+1
else:
    for val,valocc in d.items():
        print("\t{}-->{}".format(val,valocc))



