#Program for Demonstrating Data Encapsulation
#Account2.py<-----File Name and Module Name
class Account:
	def getAccDet(self):
		self.__acno=10				 # Data Encapsulation at Data Member Level through Method
		self.cname="RS"
		self.__bal=4.5
		self.__pin=1234
		self.bname="SBI"

