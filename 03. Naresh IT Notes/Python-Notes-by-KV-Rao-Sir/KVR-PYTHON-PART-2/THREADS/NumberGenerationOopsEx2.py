#Thread Based Application for 1 to n numbers where n is +ve after every second
#NumberGenerationOopsEx2.py
import threading,time
class Numbers:
	def  numbergenerate(self,n): # Instance Method-----
		if(n<=0):
				print("{}---> {} Invalid Input:".format(threading.current_thread().name,n))
		else:
				print("-----------------------------------------------------------")
				print("{}-->Numbers within:{}".format(threading.current_thread().name,n))
				print("-----------------------------------------------------------")
				for i in range(1,n+1):
					print("\tVal of i={}".format(i))
					time.sleep(0.25)
				print("-----------------------------------------------------------")
		
#Main Program
n=int(input("Enter How Many Numbers u want to generate:"))
t1=threading.Thread(target=Numbers().numbergenerate,args=(n,))
t1.name="number genarator"
t1.start()
#Numbers().numbergenerate is called Name-Less Object Creation