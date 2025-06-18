#DecEx1.py
def  getval():   # This Fun defined by KVR
	return float(input("Enter a Number:"))

def  square(kvr): # square is called called Decorator (OR) Outer Function
	def calculation(): # here calculation is called Inner Function
		k=kvr()
		res=k**2
		return k,res
	return calculation

#Main Program
calc=square(getval) # Function call--takes Normal Function Name as an Argument--hence it is Decorator Function Call
#here calc is variable in main program which is holding the Reference of inner function calculation
gv,sqv=calc()
print("square({})={}".format(gv,sqv))