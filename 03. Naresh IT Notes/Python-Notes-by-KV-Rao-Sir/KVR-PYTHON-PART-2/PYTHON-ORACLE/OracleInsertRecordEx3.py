#Program for Inserting Record in employee Table
#OracleInsertRecordEx3.py
import oracledb as orc
def recordinsert():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/orcl")
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
        except orc.DatabaseError as db:
            print("Problem in Oracle DB: ",db)
#Main Program
recordinsert() # Function Call
