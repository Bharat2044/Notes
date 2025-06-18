#Write a python programm which demonstrates obtaining the connection from Oracle data base
#OracleConnTest1.py
import oracledb as orc # Step-1
try:
    conn=orc.connect("system/tiger@localhost/orcl") # Step-2
    print("Python Program Obtains Connection from Oracle DB")
    print("Type of conn=",type(conn))
except orc.DatabaseError as db:
    print("invalid username/password; logon denied")
