#ClientDBEx.py
import socket
s=socket.socket()
s.connect(("localhost",6666))
empno=input("Enter Employee Number for Getting Other Details:")
s.send(empno.encode())
empdet=s.recv(1024).decode()
print("Employee Details")
print("--------------------------------------")
print(empdet)
print("--------------------------------------")