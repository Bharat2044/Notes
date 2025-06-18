#Program for Demonstrating Execution of Multiple threads and Execution time
#MultipleThreadExecutionEx.py
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
#create a sub thread t1 for executing Squares
t1=threading.Thread(target=squares,args=(lst,))
#create a sub thread t2 for executing Cubes
t2=threading.Thread(target=cubes,args=(lst,))
t1.start()
t2.start()
#Make MainThread to Wait until sub threads Joins with MainThread
t1.join()
t2.join()
print("Execution Status of t1 after join=",t1.is_alive())
print("Execution Status of t2 after join=",t2.is_alive())
print("Program Execution Ended:{}".format(threading.current_thread().name))
et=time.time()
print("Total Execution of Time this program--single threaded={}".format(et-bt))