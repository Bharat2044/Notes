#Program for Demonstrating How Multiple Sub Thread will execute all the functions and main program entries
#SubThreadFlow.py
import threading
def hello():
	print("hello()--Executed by=",threading.current_thread().name)
def welcome():
	print("welcome()--Executed by=",threading.current_thread().name)
def hi():
	print("hi()--Executed by=",threading.current_thread().name)

#main Program
print("Program Execution Started by :",threading.current_thread().name)
print("------------------------------")
#create Sub Thread t1--name Thread-1
t1=threading.Thread(target=hello)
t1.name="KVR"
t1.start()
print("------------------------------")
#create Sub Thread t2name Thread-2
t2=threading.Thread(target=welcome)
t2.start()
print("------------------------------")
#create Sub Thread t3name Thread-3
t3=threading.Thread(target=hi)
t3.start()
print("------------------------------")
t1.join()
t2.join()
t3.join()
print("Program Execution Ended by :",threading.current_thread().name)

