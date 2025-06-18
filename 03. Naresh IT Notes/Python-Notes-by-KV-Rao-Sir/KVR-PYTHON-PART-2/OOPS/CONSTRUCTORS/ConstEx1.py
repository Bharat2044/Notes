#Program for Demonstrating the need of Constructors
#ConstEx1.py
class Employee:
	def  __init__(self):  # Default OR Parameter-Less Constructor
		print("I am from Default Constructor")
		self.eno=100
		self.ename="Rossum"
		self.sal=45
		print("---------------------------------")
		print("Emp Number:{}".format(self.eno))
		print("Emp Name:{}".format(self.ename))
		print("Emp Sal:{}".format(self.sal))
		print("---------------------------------")
	

#Main Program
eo1=Employee() # Whenever we create an object, I want place our own data without leaving an object empty
eo2=Employee() # Whenever we create an object, I want place our own data without leaving an object empty


