#FileOpenEx1.py
import sys
try:
    fp=open("kvr1.data","r")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("File Open Sucessfully in Read Mode")
finally:
    print("I am from Finally Block--File Closed")
    fp.close()