#Write a python programm which demonstrates obtaining the connection from Oracle data base
#OracleConnTest2.py
import oracledb as orc # Step-1
try:
    conn=orc.connect("system/tiger@127.0.0.1/orcl") # Step-2
except orc.DatabaseError as db:
    print("invalid username/password; logon denied")
else:
    print("Python Program Obtains Connection from Oracle DB")
    print("Type of conn=", type(conn))