#Program for Demonstrating Destructor 
#GCEX2.py
import sys,time,gc
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterised Constructor")
		self.eno=eno
		self.ename=ename
		print("Emp Num:{}".format(self.eno))
		print("Emp Name:{}".format(self.ename))
		print("-----------------------------------------------")
	def __del__(self):
		global totmem
		print("__del__() called by GC to de-allocating memory space--Object id=",id(self))
		totmem=totmem-sys.getsizeof(self)
		print("Now Available Memory Space=",totmem)

#Main program
print("Program Execution Started:")
print("Initially, Is GC Running=",gc.isenabled())
e1=Employee(10,"RS") # Object Creation--Makes the PVM To call Parameterized Constructor
e2=Employee(20,"DR") # Object Creation--Makes the PVM To call Parameterized Constructor
e3=Employee(30,"TR") # Object Creation--Makes the PVM To call Parameterized Constructor
totmem=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
gc.disable()
print("ID of e1=",id(e1))
print("ID of e2=",id(e2))
print("ID of e3=",id(e3))
print("TOTAL MEMORY SPACE OF ALL OBJECT=",totmem) # 144
print("Is GC Running after disable()=",gc.isenabled())
print("Program Execution Ended:")
time.sleep(10)
