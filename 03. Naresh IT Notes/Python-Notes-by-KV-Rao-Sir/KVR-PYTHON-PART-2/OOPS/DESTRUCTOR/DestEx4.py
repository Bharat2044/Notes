#Program for Demonstrating Destructor ------Forceful Garbage Collection
#DestEx4.py
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
print("No Longer Interested in Maintaining Object e1 Memory Space")
time.sleep(4)
del e1  # Making the GC to Destructor Forcefully
time.sleep(3)
e2=Employee(20,"DR") # Object Creation--Makes the PVM To call Parameterized Constructor
print("No Longer Interested in Maintaining Object e2 Memory Space")
time.sleep(4)
del e2  # Making the GC to Destructor Forcefully
time.sleep(3)
e3=Employee(30,"TR") # Object Creation--Makes the PVM To call Parameterized Constructor
print("No Longer Interested in Maintaining Object e3 Memory Space")
time.sleep(3)
del e3 # Making the GC to Destructor Forcefully
time.sleep(3)
print("Program Execution Ended:")
