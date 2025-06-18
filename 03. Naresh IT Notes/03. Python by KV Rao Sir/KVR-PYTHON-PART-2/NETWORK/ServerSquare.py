#a) Write a Server Program in such way that It should a accept a number from Client Side Program Square It and Gives Response Back to Client Side Program.
#ServerSquare.py
import socket  # step-1
s=socket.socket() # step-2
s.bind(("localhost",8888)) #step-3
s.listen(2) # Step-4
print("SSP is Ready to accept any CSP Request")
while(True):
	try:
		cs,ca=s.accept() # Step-5
		#step-6
		cval=cs.recv(1024).decode()
		print("Val of Client at Server=",cval)
		cv=float(cval)
		res=cv**2
		cs.send(str(res).encode()) # Step-7
	except ValueError:
		cs.send("Don't Enter alnums,strs and symbols".encode())








