#Program for Demonstrating How Single Thread will execute all the functions and main program entries
#DefaultThreadFlow.py
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
hello()
print("------------------------------")
welcome()
print("------------------------------")
hi()
print("------------------------------")
print("Program Execution Ended by :",threading.current_thread().name)

