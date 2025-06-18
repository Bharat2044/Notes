#Program for Demonstrating global keyword
#GlobalKwdEx2.py
def  updatation1():
	global a,b # Which Refers Global Values Mandatory to write
	a=a+1 # Here we are modifying the global Var Value
	b=b+1 # Here we are modifying the global Var Value

def  updatation2():
	global a,b # Which Refers Global Values Mandatory to write
	a=a*2  # Here we are modifying the global Var Value
	b=b*2 # Here we are modifying the global Var Value

def  updatation3():
	x=a+1 #Here we are not modifying the global Var Value and we are Just Accessing the Value. So that No need to 
	            #write global kwd
	y=b+2
	print("Local value x=",x) # 23
	print("Local Value y=",y) # 44
#Main program
a=10
b=20 # Here a and b are called Global Variables
print("In Main Program before updation1()  a={}  b={}".format(a,b)) # a=10  b=20
updatation1() # Function call
print("In Main Program after updatation1()  a={}  b={}".format(a,b))  # a=11  b=21
updatation2()
print("In Main Program after updatation2() a={}  b={}".format(a,b))  # a=22  b=42
updatation3()
print("In Main Program after updatation3()  a={}  b={}".format(a,b))  # a=22  b=42