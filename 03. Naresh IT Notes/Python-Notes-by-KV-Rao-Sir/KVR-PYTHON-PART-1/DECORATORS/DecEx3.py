#DecEx3.py
def cube( hyd):
	def compute():
		n,sq=hyd()
		cb=n**3
		return n,sq,cb
	return compute

def square(kvr):
	def calculation():
		k=kvr()
		res=k**2
		return k,res
	return calculation

@cube
@square
def  getval():   # This Fun defined by KVR
	return float(input("Enter a Number:"))
#Main Program
n,sqv,cbv=getval() # Normal Function
print("square({})={}".format(n,sqv))
print("Cube({})={}".format(n,cbv))
