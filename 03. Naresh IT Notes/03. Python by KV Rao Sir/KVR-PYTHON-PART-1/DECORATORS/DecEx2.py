#DecEx2.py
def square(kvr):
	def calculation():
		k=kvr()
		res=k**2
		return k,res
	return calculation

@square
def  getval():   # This Fun defined by KVR
	return float(input("Enter a Number:"))

#Main Program
n,sqv=getval() # Normal Function
print("square({})={}".format(n,sqv))
