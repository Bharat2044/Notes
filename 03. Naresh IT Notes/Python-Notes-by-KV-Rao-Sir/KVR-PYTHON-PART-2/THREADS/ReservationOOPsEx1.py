#Program for Showing Reversevation System
#ReservationOOPsEx1.py
import threading,time
class Train:
	@classmethod
	def getLock(cls):
		cls.L=threading.Lock()
		cls.totseats=10  # Here L and totseats are called Class Level Variables
		print("Total Number of Seats:{}".format(cls.totseats))

	def __init__(self,nos):
		self.nos=nos

	def  reservation(self):
		Train.L.acquire()
		if(self.nos>Train.totseats):
			print("Hi {}, {} are Not Available-try for next time".format(threading.current_thread().name,self.nos))
			time.sleep(2)
		else:
			Train.totseats=Train.totseats-self.nos
			print("Hi {}, {} Seats Reserved-Hpy Journey".format(threading.current_thread().name,self.nos))
			print("Available Seats={}".format(Train.totseats))
			time.sleep(2)
			if(Train.totseats==0):
				print("Train is Full")
		Train.L.release()

#Main Program
Train.getLock()
p1=threading.Thread(target=Train(3).reservation)
p2=threading.Thread(target=Train(4).reservation)
p3=threading.Thread(target=Train(6).reservation)
p4=threading.Thread(target=Train(2).reservation)
p5=threading.Thread(target=Train(3).reservation)
p6=threading.Thread(target=Train(1).reservation)
#dispatch the Threads (Passengers)
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()


