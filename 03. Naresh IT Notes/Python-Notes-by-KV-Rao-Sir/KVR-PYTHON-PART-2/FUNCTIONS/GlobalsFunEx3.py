#Program for Demonstrating globals()
#In This Program we are observing Local Var Names  and Global Var Names are SAME. 
#GlobalsFunEx3.py
a=10
b=20
c=30
d=40 # Here a,b,c,d are called global variables
def  operation():
	a=1
	b=2
	c=3
	d=4 # Here a,b,c,d are called Local Variables
	print("--------------------------------------------------------")
	print("List of Local Variable Values")
	print("\tVal of a=",a)
	print("\tVal of b=",b)
	print("\tVal of c=",c)
	print("\tVal of d=",d)
	print("---------------------------------------------------------")
	print("List of Global Variable Values")
	print("\tVal of a=",globals().get('a'))
	print("\tVal of b=",globals().get('b'))
	print("\tVal of c=",globals().get('c'))
	print("\tVal of d=",globals().get('d'))
	print("---------------------------------------------------------")
	res=a+b+c+d+globals()['a']+globals()['b']+globals().get('c')+globals().get('d')
	print("Res=",res)

#Main program
operation()

