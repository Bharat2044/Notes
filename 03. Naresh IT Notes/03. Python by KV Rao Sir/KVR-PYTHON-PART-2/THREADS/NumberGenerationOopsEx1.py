#Thread Based Application for 1 to n numbers where n is +ve after every second
#NumberGenerationOopsEx1.py
import threading,time
class Numbers:
	def  numbergenerate(self): # Instance Method-----
		try:
			n=int(input("Enter How Many Numbers u want to generate:"))
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
		except ValueError:
			print("Don't Enter alnums,strs and symbols")

#Main Program
no=Numbers() # Object Creation specially for calling Instance Method
t1=threading.Thread(target=no.numbergenerate)
t1.name="number genarator"
t1.start()