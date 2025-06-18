#Program for Demonstrating Getting Default Thread
#DefaultThreadName.py
import threading
tname=threading.current_thread().name
print("Default Thread Name:",tname)
print("Number of Active Threads by Default=", threading.active_count())