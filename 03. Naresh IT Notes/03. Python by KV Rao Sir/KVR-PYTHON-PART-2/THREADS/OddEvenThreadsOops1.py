#Program for Generating Odd and Even Numbers by using Multiple Threads 
#OddEvenThreadsOops1.py
import threading,time
class OddNums:
	def odd(self,n):
		if(n<=0):
			print("{}--->{} Is Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(1,n+1,2):
				print("{}--->Odd:{}".format(threading.current_thread().name,i))
				time.sleep(1)

class EvenNums:
	def even(self,n):
		if(n<=0):
			print("{}--->{} Is Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(2,n+1,2):
				print("{}--->Even:{}".format(threading.current_thread().name,i))
				time.sleep(1)

#Main Program
on=int(input("Enter How Many Odd Numbers u want:"))
en=int(input("Enter How Many Even Numbers u want:"))
t1=threading.Thread(target=OddNums().odd,args=(on,))
t2=threading.Thread(target=EvenNums().even,args=(en,))
t1.name="ODD"
t2.name="EVEN"
t1.start()
t2.start()