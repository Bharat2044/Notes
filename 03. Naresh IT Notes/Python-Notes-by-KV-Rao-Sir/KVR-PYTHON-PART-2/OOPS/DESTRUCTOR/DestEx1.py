#Program for Demonstrating Destructor 
#DestEx1.py
import time
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterised Constructor")
		self.eno=eno
		self.ename=ename
		print("Emp Num:{}".format(self.eno))
		print("Emp Name:{}".format(self.ename))
		print("-----------------------------------------------")
	def __del__(self):
		print("__del__() called by GC to de-allocating memory space")
	
#Main program
print("Program Execution Started:")
e1=Employee(10,"RS") # Object Creation--Makes the PVM To call Parameterized Constructor
e2=Employee(20,"DR") # Object Creation--Makes the PVM To call Parameterized Constructor
e3=Employee(30,"TR") # Object Creation--Makes the PVM To call Parameterized Constructor
print("Program Execution Ended:")


#Here GC calls  __del__ (Destructor) at the end of Program Execution--This Process is called called Automatic Garbage Collection
