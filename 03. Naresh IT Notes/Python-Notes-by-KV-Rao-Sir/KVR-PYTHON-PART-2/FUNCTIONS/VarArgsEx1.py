#Program for demonstrating the Need of Variable Length Arguments
#Conclusion:---This Program will not execute bcoz PVM Remembers Latest Function Defintion bcoz of PVM is performing Interpretation.
#VarArgsEx1.py
def disp(a,b,c,d,e): # Function Def-1 with 5 params
	print(a,b,c,d,e)

def disp(a,b,c,d): # Function Def-2 with 4 params
	print(a,b,c,d)
def disp(a,b,c): # Function Def-3 with 3 params
	print(a,b,c)

def disp(a,b): # Function Def-4 with 2 params
	print(a,b)
def disp(a): # Function Def-5 with 1 param
	print(a)

#Main Program
disp(10,20,30,40,50) # Function Call-1 with   5 Args
disp(10,20,30,40) # Function Call-2 with   4 Args
disp(10,20,30) # Function Call-3 with   3 Args
disp(10,20) # Function Call-3 with   2 Args
disp(10) # Function Call-3 with   1 Args