#b) Write a Client Program in such way that It Must read a number from key board, send it to Server Program and  Get Its Square from server Program.
#ClientSquare.py
import socket # Step-1
s=socket.socket() # Step-2
s.connect(("localhost",8888)) # Step-3
#Step-4
val=input("Enter a number for getting its square:")
s.send(val.encode())
#Step-5
sval=s.recv(1024).decode()
print("square({})={}".format(val,sval))
