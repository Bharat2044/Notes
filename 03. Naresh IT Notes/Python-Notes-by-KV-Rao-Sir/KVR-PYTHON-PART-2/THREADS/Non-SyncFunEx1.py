#Program for Showing Dead Lock Result
#Non-SyncFunEx1.py
import threading,time
def  table(n):
	if(n<=0):
		print("{}--->{}-->Is Invalid Input".format(threading.current_thread().name,n))
	else:
		print("Mul Table for :{}".format(n))
		for i in range(1,11):
				print("{}-->{} x {} = {}".format(threading.current_thread().name,n,i,n*i))
				time.sleep(1)
		print("----------------------------------------")

#Main program
t1=threading.Thread(target=table,args=(7,))
t2=threading.Thread(target=table,args=(17,))
t3=threading.Thread(target=table,args=(-9,))
t4=threading.Thread(target=table,args=(19,))
t1.start()
t2.start()
t3.start()
t4.start()

