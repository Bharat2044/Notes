#a) Write a Server Program in such way that It should a accept a number from Client Side Program Square It and Gives Response Back to Client Side Program.
#ServerSquare.py
import socket
s=socket.socket() # step-1
s.bind(("localhost",8888)) #step-2
s.listen(2)
print("SSP is Ready to accept any CSP Request")
#lots of Code
