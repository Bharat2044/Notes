#Program for Demonstrating Creating a Table--employee
#MySQLTableCreateEx.py
import mysql.connector
def tablecreate():
    try:
        con=mysql.connector.connect(host="127.0.0.1",
                                    user="root",
                                    passwd="root",
                                    database="kvr")
        cur=con.cursor()
        #Table creation Query
        tq="create table student(sno int primary key,name varchar(10) not null,marks float not null)"
        cur.execute(tq)
        print("Table Created--Verify")
    except mysql.connector.DatabaseError as db:
        print("Priblem in MySQL: ",db)

#Main Program
tablecreate()