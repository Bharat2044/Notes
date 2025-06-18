#Program for Demonstrating globals()
#In This Program we are observing Local Var Names  and Global Var Names are Unique. So that there is no problem in accessing
#GlobalsFunEx2.py
a=10
b=20
c=30
d=40 # Here a,b,c,d are called global variables
def  operation():
	x=1
	y=2
	z=3
	k=4 # Here x,y,z,k are called Local Variables
	res=a+b+c+d+x+y+z+k
	print("Res=",res)

#Main program
operation()

