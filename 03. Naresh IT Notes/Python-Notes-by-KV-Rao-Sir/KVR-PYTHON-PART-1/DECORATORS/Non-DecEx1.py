#Non-DecEx1.py
def  getval():   # This Fun defined by KVR
	return float(input("Enter a Number:")) 

def square():						#Girish--Student--Sir give me square of ur number
	n=getval()
	res=n**2
	print("square({})={}".format(n,res))

def squareroot():						#Sumit --Student--Sir give me square root of ur number
	n=getval()
	res=n**0.5
	print("squareroot({})={}".format(n,res))

def cube():						#Jain--Student--Sir give me cube root of ur number
	n=getval()
	res=n**3
	print("cube({})={}".format(n,res))

def root4th():						#Usha--Student--Sir give me 4th root of ur number
	n=getval()
	res=n**(1/4)
	print("4throot({})={}".format(n,res))

#Main Program
square()
squareroot()
cube()
root4th()