#Program for Inserting Record in employee Table
#OracleInsertRecordEx2.py
import oracledb as orc
def recordinsert():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Accept employees values from KBD
        eno=int(input("Enter Employee Number:"))
        empname=input("Enter Employee Name:")
        sal=float(input("Enter Employee Salary:"))
        cname=input("Enter Employee Comp Name:")
        #Design the Query
        iq="insert into employee values(%d,'%s',%f,'%s')"
        cur.execute(iq %(eno,empname,sal,cname))
        con.commit()
        print("Employee Record Inserted Successfully--Verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB: ",db)
#Main Program
recordinsert() # Function Call
