#program for Demonstrating How to set Name and get name of sub threads
#SetGetThreadEx.py
import threading
def hello():
	print("\t\thello() executed by :{}".format(threading.current_thread().name))

#main Program
t1=threading.Thread(target=hello) # here t1 is object and whose name is Thread-1
#tname=t1.getName() # Here getName() deprecated on the name of "name" attribute
tname=t1.name
print("Sub Thread Name:",tname)
#t1.setName("HYD")   # Here setName() deprecated on the name of "name" attribute
t1.name="HYD"  # Acts like setName()
tname=t1.name  # Acts Like getName()
print("Sub Thread Name:",tname)

