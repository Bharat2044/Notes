#Program for Demonstrating globals()
#In This Program we are observing Local Var Names  and Global Var Names are SAME. 
#GlobalsFunEx4.py
a=10
b=20
c=30
d=40   # Here a,b,c,d are called global variables
def  operation():
	x=globals() # Current Program Global Var Values + Gets Invisible global Variables of Python Exec. Ebv
	print("Programmer-Defined Global Variables--way-1")
	print("Global Value a={}".format(x['a']))
	print("Global Value b={}".format(x['b']))
	print("Global Value c={}".format(x['c']))
	print("Global Value d={}".format(x['d']))
	print("Programmer-Defined Global Variables--way-2")
	print("Global Value a={}".format(x.get('a')))
	print("Global Value b={}".format(x.get('b')))
	print("Global Value c={}".format(x.get('c')))
	print("Global Value d={}".format(x.get('d')))
	print("Programmer-Defined Global Variables--way-3")	
	print("Global Value a=",globals()['a'])
	print("Global Value b=",globals()['b'])
	print("Global Value c=",globals()['c'])
	print("Global Value d=",globals()['d'])
	print("Programmer-Defined Global Variables--way-4")	
	print("Global Value a=",globals().get('a'))
	print("Global Value b=",globals().get('b'))
	print("Global Value c=",globals().get('c'))
	print("Global Value d=",globals().get('d'))

#Main Program
operation()
	
