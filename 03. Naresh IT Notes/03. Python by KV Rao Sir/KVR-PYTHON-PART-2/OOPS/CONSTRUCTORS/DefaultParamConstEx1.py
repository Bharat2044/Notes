#Program for Deomstrating Default and Parametrized Constructor in single class
#DefaultParamConstEx1.py
class Test:
	def __init__(self,p=1,q=2): # Acts as Deafult and Parametrized  Constructor
		print("------------------------------------------------")
		print("I am from Default / Parametrized Constructor")
		self.a=p
		self.b=q
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("------------------------------------------------")

#Main program
t1=Test() # Object Creation---Makes the PVM to call Default  Constructor
t2=Test(10,20) # Object Creation---Makes the PVM to call Parametrized Constructor
t3=Test(100) # Object Creation---Makes the PVM to call Parametrized Constructor
t4=Test(q=100) # Object Creation---Makes the PVM to call Parametrized Constructor
t4=Test(q=200,p=300) # Object Creation---Makes the PVM to call Parametrized Constructor
