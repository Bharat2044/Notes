#Program for Demonstrating Garbage Collector Existence
#GCEX1.py
import gc
print("Program Execution Started")
print("Initially, Is GC Running=",gc.isenabled())
a=10
b=20
c=a+b
gc.disable()
print("Is GC Running after disable()=",gc.isenabled())
print("Val of a=",a)
print("Val of b=",b)
gc.enable()
print("Is GC Running after enable()=",gc.isenabled())
print("Sum=",c)
print("Program Execution Ended")
