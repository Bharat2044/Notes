#Program for Demonstrating How to obtain Connection from mySQL
#MySQLConnTestEx2.py
import mysql.connector
try:
    con=mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                passwd="root")
    print("Python Program Obtains Connection from MySQL")
    print("type of con=",type(con))
except mysql.connector.DatabaseError as d:
    print("Problem in MySQL :",d)