#ServerChat.py
import socket
s=socket.socket()
s.bind(("127.0.0.1",9999))
s.listen(2)
while(True):
	cs,ca=s.accept()
	cdata=cs.recv(1024).decode()
	print("Student :{}".format(cdata))
	sdata=input("Teacher:")
	cs.send(sdata.encode())





