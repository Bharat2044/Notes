#Program for Demonstrating Data Encapsulation
#Account1.py<-----File Name and Module Name
class Account:
	def __init__(self):
		self.__acno=10		# Data Encapsulation at Data Member Level through Constructor
		self.cname="RS"
		self.__bal=4.5
		self.__pin=1234
		self.bname="SBI"

