#ServerDBEx.py
import socket as sock
import oracledb as orc
s=sock.socket()
s.bind(("localhost",6666))
s.listen(1)
print("SSP is ready to accept any request")
while(True):
	try:
		csock,caddr=s.accept()
		eno=int(csock.recv(1024).decode())
		#Write PDBC
		con=orc.connect("system/tiger@localhost/orcl")
		cur=con.cursor()
		cur.execute("select * from employee where eno=%d" %eno)
		record=cur.fetchone()
		if(record==None):
			csock.send("No Record Exist".encode())
		else:
			s1="Emp Number:"+str(record[0])
			s2="Emp Name:"+str(record[1])
			s3="Emp Salary:"+str(record[2])
			s4="Emp Comp Name:"+str(record[3])
			res=s1+"\n"+s2+"\n"+s3+"\n"+s4
			csock.send(res.encode())
			
	except ValueError:
		csock.send("Don't enter alnums,strs and symbols for empno".encode())
	except orc.DatabaseError as db:
		print("Problem in Oracle:",db)