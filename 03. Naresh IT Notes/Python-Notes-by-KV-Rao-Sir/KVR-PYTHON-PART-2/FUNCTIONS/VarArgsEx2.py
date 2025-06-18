#Program for demonstrating the Need of Variable Length Arguments
#Conclusion:---This Program will execute bcoz PVM takes the Definition and Immediately calls
#VarArgsEx2.py
def disp(a,b,c,d,e): # Function Def-1 with 5 params
	print(a,b,c,d,e)
disp(10,20,30,40,50) # Function Call-1 with   5 Args
#------------------------------------------------------------------------
def disp(a,b,c,d): # Function Def-2 with 4 params
	print(a,b,c,d)
disp(10,20,30,40) # Function Call-2 with   4 Args
#------------------------------------------------------------------------
def disp(a,b,c): # Function Def-3 with 3 params
	print(a,b,c)
disp(10,20,30) # Function Call-3 with   3 Args
#------------------------------------------------------------------------
def disp(a,b): # Function Def-4 with 2 params
	print(a,b)
disp(10,20) # Function Call-3 with   2 Args
#------------------------------------------------------------------------
def disp(a): # Function Def-5 with 1 param
	print(a)
disp(10) # Function Call-3 with   1 Args
#------------------------------------------------------------------------

#LIMITATION:  
#we have 5 Similar Function Calls with Variable Args then We defined 5 Function Defs with Variable Parms
#In General If we have 1000 Similar Function Calls with Variable Args We defined 1000 Function Defs with Variable Parms.This Process Leads to Time Consuming



