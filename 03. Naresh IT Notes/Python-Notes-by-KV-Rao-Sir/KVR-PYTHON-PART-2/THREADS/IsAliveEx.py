#program for Demonstrating to chech the execution status of sub threads
#IsAliveEx.py
import threading
def hello():
	print("\t\thello() executed by :{}".format(threading.current_thread().name))

#main Program
t1=threading.Thread(target=hello)
print("{}---Is t1 is running before start()={}".format(threading.current_thread().name,t1.is_alive()))
t1.start()
print("{}---Is t1 is running after start()={}".format(threading.current_thread().name,t1.is_alive()))