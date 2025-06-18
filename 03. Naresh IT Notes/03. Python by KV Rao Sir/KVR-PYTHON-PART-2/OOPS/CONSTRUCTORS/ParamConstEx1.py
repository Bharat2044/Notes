#Program for Deomstrating Parametrized Constructor
#ParamConstEx1.py
class Test:
	def __init__(self,p,q): # Parametrized  Constructor
		print("------------------------------------------------")
		print("I am from Parametrized Constructor")
		self.a=p
		self.b=q
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("------------------------------------------------")

#Main program
t1=Test(10,20) # Object Creation---Makes the PVM to call Parametrized  Constructor
t2=Test(100,200) # Object Creation---Makes the PVM to call Parametrized Constructor
t3=Test(1000,2000) # Object Creation---Makes the PVM to call Parametrized Constructor

