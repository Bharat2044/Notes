#Program for Demonstrating Destructor ------Forceful Garbage Collection
#DestEx5.py
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
e2=e1 # Deep Copy
e3=e2 # Deep Copy
print("Program Execution Ended:")
#Here e1,e2,e3 participates in DEEP COPY, So that GC calls Destructor Only Once bcoz all the objects contains Same Address