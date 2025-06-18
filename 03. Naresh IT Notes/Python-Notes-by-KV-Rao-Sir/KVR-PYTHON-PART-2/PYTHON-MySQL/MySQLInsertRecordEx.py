#Program for Inserting Record in employee Table
#MySQLInsertRecordEx.py
import mysql.connector
def recordinsert():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="7ambatch")
            cur=con.cursor()
            #Accept employees values from KBD
            print("-" * 50)
            eno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            sal=float(input("Enter Employee Salary:"))
            cname=input("Enter Employee Comp Name:")
            #Design the Query
            iq="insert into employee values(%d,'%s',%f,'%s')"
            cur.execute(iq %(eno,empname,sal,cname))
            con.commit()
            print("-" * 50)
            print("Employee Record Inserted Successfully--Verify")
            print("-"*50)
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this Program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB: ",db)
#Main Program
recordinsert() # Function Call
