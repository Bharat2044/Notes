#Program for Computing Sum of Two List Objects where they Must contain Equal Elements
#MapEx4.py
print("Enter List of Values for First List Separated by Space:")
lst1=[float(val) for val in input().split()]
print("Enter List of Values for Second List Separated by Space:")
lst2=[float(val) for val in input().split()]
#Expected Output lst3=[110,220,330,440,550]
lst3=list(map(lambda x,y:x+y, lst1,lst2 ))
print("*"*50)
print("First List\t\tSecond List\t\tSum List")
print("*"*50)
for fl,sl,rs in zip(lst1,lst2,lst3):
    print("\t{}\t\t\t{}\t\t\t\t{}".format(fl,sl,rs))
print("*"*50)

