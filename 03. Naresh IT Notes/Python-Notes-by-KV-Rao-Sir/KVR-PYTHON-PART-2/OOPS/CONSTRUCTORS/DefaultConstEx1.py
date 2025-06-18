#Program for Deomstrating Default Constructor
#DefaultConstEx1.py
class Test:
	def __init__(self): # Default Constructor
		print("------------------------------------------------")
		print("I am from Default Constructor")
		self.a=10
		self.b=20
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("------------------------------------------------")

#Main program
t1=Test() # Object Creation---Makes the PVM to call Default Constructor
t2=Test() # Object Creation---Makes the PVM to call Default Constructor
t3=Test() # Object Creation---Makes the PVM to call Default Constructor

