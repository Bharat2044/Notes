#Program for Demonstrating the need of Constructors
#Non-ConstEx.py
class Employee:
	def getempvals(self): # Instance Method
		self.eno=100
		self.ename="Rossum"
		self.sal=45


#Main Program
eo=Employee() # Created with Empty Data
print("content of eo=",eo.__dict__) # { }
eo.getempvals() # Explicitly we are calling Instance method
print("content of eo=",eo.__dict__) # {............. }


