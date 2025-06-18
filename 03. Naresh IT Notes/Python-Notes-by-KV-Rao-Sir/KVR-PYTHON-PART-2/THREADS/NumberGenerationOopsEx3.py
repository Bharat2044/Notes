#Thread Based Application for 1 to n numbers where n is +ve after every second
#NumberGenerationOopsEx3.py
import threading,time
class Numbers:
	def __init__(self,n):
		self.n=n

	def  numbergenerate(self): # Instance Method-----
		if(self.n<=0):
				print("{}---> {} Invalid Input:".format(threading.current_thread().name,self.n))
		else:
				print("-----------------------------------------------------------")
				print("{}-->Numbers within:{}".format(threading.current_thread().name,self.n))
				print("-----------------------------------------------------------")
				for i in range(1,self.n+1):
					print("\tVal of i={}".format(i))
					time.sleep(0.25)
				print("-----------------------------------------------------------")
		
#Main Program
n=int(input("Enter How Many Numbers u want to generate:"))
no=Numbers(n)# Object Creation---Calls Constructor
t1=threading.Thread(target=no.numbergenerate)
t1.name="number genarator"
t1.start()
#Numbers().numbergenerate is called Name-Less Object Creation