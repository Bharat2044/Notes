#Program for demonstrating the Need of Variable Length Arguments
#This Program accept sno,name and also accepts Variable Number of Values and  Calculating sum of Variable Number of Values
#PureVarArgsEx4.py
def  disp(sno,sname, *a): # here *a is called Variable Length Parameter whose type tuple
	print("------------------------------------")
	print("Student Number=",sno)
	print("Student Name=",sname)
	s=0
	for val in a:
			print("{}".format(val),end="  ")
			s+=val
	print()
	print("sum=",s)
	print("-------------------------------------------")

#Main Program
disp(100,"RS",10,20,30,40,50) # Function Call-1 with   5 Args
disp(200,"TR",10,20,30,40) # Function Call-2 with   4 Args
disp(300,"DR",10,20,30) # Function Call-3 with   3 Args
disp(400,"SS",10,20) # Function Call-4 with   2 Args
disp(500,"GR",10) # Function Call-5with   1 Args
disp(600,"AR") # Function Call-6 with   1 Args