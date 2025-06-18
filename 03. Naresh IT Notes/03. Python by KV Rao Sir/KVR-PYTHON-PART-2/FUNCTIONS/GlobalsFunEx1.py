#Program for Demonstrating globals()
#In This Program we are observing Local Var Names  and Global Var Names are SAME. 
#GlobalsFunEx1.py
a=100
b=200 # Here a, b are called global variables
def  operation():
	x=globals() # Current Program Global Var Values + Gets Invisible global Variables of Python Exec. Env
	print("Invisible Global Variables")
	print("Number of Invisible Global Variables=",len(x))
	for gvn,gvv in x.items():
		print("{}-->{}".format(gvn,gvv))
	

#Main Program
operation()
	
