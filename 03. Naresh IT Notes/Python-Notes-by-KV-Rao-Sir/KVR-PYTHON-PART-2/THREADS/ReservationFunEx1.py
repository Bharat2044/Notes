#Program for Showing Reversevation System
#ReservationFunEx1.py
import threading,time
def  reservation(nos):
	L.acquire()
	global totseats
	if(nos>totseats):
		print("Hi {}, {} are Not Available-try for next time".format(threading.current_thread().name,nos))
		time.sleep(2)
	else:
		totseats=totseats-nos
		print("Hi {}, {} Seats Reserved-Hpy Journey".format(threading.current_thread().name,nos))
		print("Available Seats={}".format(totseats))
		time.sleep(2)
		if(totseats==0):
			print("Train is Full")
	L.release()

#Main Program
L=threading.Lock()
totseats=11 
print("Total Number of Seats:{}".format(totseats))
p1=threading.Thread(target=reservation,args=(3,))
p2=threading.Thread(target=reservation,args=(4,))
p3=threading.Thread(target=reservation,args=(6,))
p4=threading.Thread(target=reservation,args=(2,))
p5=threading.Thread(target=reservation,args=(3,))
p6=threading.Thread(target=reservation,args=(1,))
#dispatch the Threads (Passengers)
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()


