#Program for Demonstrating globals() and display only Invisible globals variables and programmer defined global var
#In This Program we are observing Local Var Names  and Global Var Names are SAME. 
#GlobalsFunEx5.py
a=10
b=20
c=30
d=40   # Here a,b,c,d are called global variables
def  operation():
	print("Only Invisible Global Variable Names")
	x=globals() #  Current Program Global Var Values + Gets Invisible global Variables of Python Exec. Env
	for gvn,gvv in x.items():
		if(gvn not in ['a','b','c','d']):
			print("\t{}->{}".format(gvn,gvv))
	print("-----------------------------------------------------")
	print("Only Programmer-Defined Global Variable Names")
	for gvn,gvv in x.items():
		if(gvn in ['a','b','c','d']):
			print("\t{}->{}".format(gvn,gvv))
	print("-----------------------------------------------------")
	print("---------------------OR--------------------------------")
	print("Only Programmer-Defined Global Variable Names")
	for gvn,gvv in x.items():
		if((gvn=='a') or (gvn=='b') or (gvn=='c') or (gvn=='d')):
			print("\t{}->{}".format(gvn,gvv))
	print("-----------------------------------------------------")
	
#Main Program
operation()
	
