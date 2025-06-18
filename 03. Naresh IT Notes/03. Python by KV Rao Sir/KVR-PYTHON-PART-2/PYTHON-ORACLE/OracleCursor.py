#Program for Demonstrating Cursor object
#OracleCursor.py
import oracledb as orc # Step-1
con=orc.connect("system/tiger@localhost/orcl")#Step-2
print("Python Program Obtains connection from Oracle DB")
print("Type of con=",type(con))
cur=con.cursor()
print("Python Program created Cursor object")
print("Type of cur=",type(cur))



