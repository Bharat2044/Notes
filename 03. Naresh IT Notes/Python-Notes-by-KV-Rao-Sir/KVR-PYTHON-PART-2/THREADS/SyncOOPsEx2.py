#Program for Showing Thread Safety  Result by applying Synchronization (dead lock elimination)
#SyncOOPsEx2.py
import threading,time
class MulTable:
	@classmethod
	def getLock(cls):
		cls.L=threading.Lock() # Here L is called Class Level Variable

	def  table(self,n):
		MulTable.L.acquire()
		if(n<=0):
			print("{}--->{}-->Is Invalid Input".format(threading.current_thread().name,n))
		else:
			print("Mul Table for :{}".format(n))
			for i in range(1,11):
					print("{}-->{} x {} = {}".format(threading.current_thread().name,n,i,n*i))
					time.sleep(1)
			print("----------------------------------------")
		MulTable.L.release()

#Main program
MulTable.getLock() # Calling Class Level Method
t1=threading.Thread(target=MulTable().table,args=(7,))
t2=threading.Thread(target=MulTable().table,args=(-17,))
t3=threading.Thread(target=MulTable().table,args=(9,))
t4=threading.Thread(target=MulTable().table,args=(19,))
t1.start()
t2.start()
t3.start()
t4.start()

