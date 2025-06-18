#ClientChat.py
import socket
while(True):
	s=socket.socket()
	s.connect(("127.0.0.1",9999))
	cdata=input("Student:")
	if(cdata.lower()=="bye"):
		s.send(cdata.encode())
		break
	else:
		s.send(cdata.encode())
		sdata=s.recv(1024).decode()
		print("Teacher:{}".format(sdata))
	
