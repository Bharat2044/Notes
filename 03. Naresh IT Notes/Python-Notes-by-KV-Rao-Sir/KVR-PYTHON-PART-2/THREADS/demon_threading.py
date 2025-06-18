#demon_threading.py
import threading as th
t1=th.current_thread().name
print('No of active threads',th.active_count())
def hi():
    print('hi')
def hello():
    print('hello')
print('Current thread name started',th.current_thread().name)
hi()
hello()
print('Current thread name at end',th.current_thread().name)