#Program for Creating Database in MYSQL
#MySQLDataBaseCreateEx1.py
import mysql.connector
def createdatabase():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root")
        cur=con.cursor()
        dq="create database kvr"
        cur.execute(dq)
        print("Database Created in MySQL--verify")
    except mysql.connector.DatabaseError as db:
        print("Priblem in MySQL: ",db)

#Main program
createdatabase() # Function call