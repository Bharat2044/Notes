#Program for demonstrating the Need of Variable Length Arguments
#PureVarArgsEx2.py
def  disp( *a): # here *a is called Variable Length Parameter whose type tuple
	print("Number of Values=",len(a))
	for val in a:
			print("{}".format(val),end="  ")
	print()
	print("-------------------------------------------")

#Main Program
disp(10,20,30,40,50) # Function Call-1 with   5 Args
disp(10,20,30,40) # Function Call-2 with   4 Args
disp(10,20,30) # Function Call-3 with   3 Args
disp(10,20) # Function Call-4 with   2 Args
disp(10) # Function Call-5with   1 Args
disp()# Function Call-6 with   1 Args