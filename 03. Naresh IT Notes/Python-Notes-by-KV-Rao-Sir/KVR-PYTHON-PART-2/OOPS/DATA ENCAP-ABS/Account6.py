#Program for Demonstrating Data Encapsulation
#Account6.py
class Account:
	def __getAccDet(self): # Data Encapsulation at Method Level
		self.acno=10
		self.cname="RS"
		self.bal=4.5
		self.pin=1234
		self.bname="SBI"
	def extractdata(self):
		self.__getAccDet() # Calling Data Encapsulated Method in same class Method context
		print('Account Number:',self.acno)
		print("Account Holder Name:",self.cname)
		print('Account Bal:',self.bal)
		print("Account Pin:",self.pin)
		print("Accunt Branch Name:",self.bname)


#Main Program
ac=Account()
#ac.getAccDet()  OR ac__getAccDet()----AttributeError: 'Account' object has no attribute '__getAccDet'
ac.extractdata()
