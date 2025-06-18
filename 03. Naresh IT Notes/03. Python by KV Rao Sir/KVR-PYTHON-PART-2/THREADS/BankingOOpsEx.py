#BankingOOpsEx.py
import threading,time
class Bank:
	@classmethod
	def getLock(cls):
		cls.K=threading.Lock()
		cls.accbal=15000
	def  withdraw(self,wamt):
		Bank.K.acquire()
		if(wamt>Bank.accbal):
			print("Hi {}, INR {} Is Not Available--Check Bounce".format(threading.current_thread().name,wamt))
			time.sleep(1)
		else:
			Bank.accbal=Bank.accbal-wamt
			print("Hi {}, INR {} Is Deposit--Verify".format(threading.current_thread().name,wamt))
			time.sleep(2)
			print("Available Bal:{}".format(Bank.accbal))
		Bank.K.release()
#Main Program
Bank.getLock()
c1=threading.Thread(target=Bank().withdraw,args=(5000,))
c2=threading.Thread(target=Bank().withdraw,args=(11000,))
c3=threading.Thread(target=Bank().withdraw,args=(8000,))
c4=threading.Thread(target=Bank().withdraw,args=(5000,))
c5=threading.Thread(target=Bank().withdraw,args=(2000,))
c6=threading.Thread(target=Bank().withdraw,args=(1000,))
for obj in [c1,c2,c3,c4,c5,c6]:
	obj.start()




