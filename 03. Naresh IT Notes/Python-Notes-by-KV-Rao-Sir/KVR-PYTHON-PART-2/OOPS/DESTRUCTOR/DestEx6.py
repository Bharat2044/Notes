#Program for Demonstrating Destructor ------Forceful Garbage Collection
#DestEx6.py
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
print("No Longer Interested in Maintaining Object e1 Memory Space")
time.sleep(4)
del e1  #  GC  won't Destructor Forcefully bcoz still e2 and e3 ponits object
time.sleep(3)
print("No Longer Interested in Maintaining Object e2 Memory Space")
time.sleep(4)
e2=None  # GC  won't Destructor Forcefully bcoz still  e3 ponits object
time.sleep(3)
print("No Longer Interested in Maintaining Object e3 Memory Space")
time.sleep(4)
e3=None  # GC   calls Destructor Forcefully bcoz No Objects Points object
time.sleep(3)
print("Program Execution Ended:")
