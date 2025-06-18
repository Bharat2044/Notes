#Program for Deminstrating obtaining Default Thread
#CurrentThreadEx.py
import threading
t=threading.current_thread()
print("Default Thread Name=",t.name)
print("--------------------------------------------------")
tname=threading.current_thread().name
print("Default Thread Name=",tname)

