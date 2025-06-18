#Program for Demonstrating Execution of single thread and Execution time
#SingleThreadExecutionEx.py
import threading,time
def  squares(lst):
	for val in lst:
		print("{}---Square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)

def  cubes(lst):
	for val in lst:
		print("{}---cube({})={}".format(threading.current_thread().name,val,val**3))
		time.sleep(1)

#Main Program
bt=time.time()
print("Program Execution Started:{}".format(threading.current_thread().name))
lst=[4,12,6,18,-5,16,25,-9,2]
squares(lst)
print("-----------------------------------------------")
cubes(lst)
print("Program Execution Ended:{}".format(threading.current_thread().name))
et=time.time()
print("Total Execution of Time this program--single threaded={}".format(et-bt))