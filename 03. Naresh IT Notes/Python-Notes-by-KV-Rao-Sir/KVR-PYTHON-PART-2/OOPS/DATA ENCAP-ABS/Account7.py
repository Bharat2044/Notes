#Program for Demonstrating Data Encapsulation
#Account7.py
class Account:
	def __init__(self): # Data Encapsulation at Method Level
		self.__acno=10
		self.cname="RS"
		self.__bal=4.5
		self.__pin=1234
		self.bname="SBI"
	def extractdata(self):
		#print('Account Number:',self.acno)---Gives Error
		print('Account Number:',self.__acno)
		print("Account Holder Name:",self.cname)
		print('Account Bal:',self.__bal)
		print("Account Pin:",self.__pin)
		print("Accunt Branch Name:",self.bname)

#Main Program
ac=Account()
ac.extractdata()
