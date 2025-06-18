#Program for Deminstrating obtaining number of active threads
#ActiveThreadCountEx.py
import threading
tname=threading.current_thread().name
print("Default Thread Name=",tname)
noact=threading.active_count()
print("Number of Active Threads=",noact)
