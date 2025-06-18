#Program for Demonstrating the need of Constructors
#ConstEx2.py
class Employee:
	def  __init__(self,eno,ename,sal): # Parameterized Constructor
		print("I am from Parameterized Constructor ")
		self.eno=eno
		self.ename=ename
		self.sal=sal
		print("---------------------------------")
		print("Emp Number:{}".format(self.eno))
		print("Emp Name:{}".format(self.ename))
		print("Emp Sal:{}".format(self.sal))
		print("---------------------------------")
	
#Main Program
eo1=Employee(100,"Rossum",45.67) # Object Creation---PVM Calls Corresponding Constructor
eo2=Employee(200,"Travis",15.45) # Object Creation---PVM Calls Corresponding Constructor




