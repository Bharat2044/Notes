#Program for Inserting Record in employee Table
#OracleInsertRecordEx4.py
import oracledb as orc
class InvalidNameError(Exception):pass
def validate(name): # name=Dheerendar Kumar Jain
    words=name.split() # words=[Dheerendar,Kum1ar, Jain]
    res=False
    for word in words:
        if(not word.isalpha()):
            res=True
            break
    if(res):
        raise InvalidNameError
    else:
        return(name)
def recordinsert():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/orcl")
            cur=con.cursor()
            #Accept employees values from KBD
            print("-" * 50)
            eno=int(input("Enter Employee Number:"))
            empname=validate(input("Enter Employee Name:"))
            sal=float(input("Enter Employee Salary:"))
            cname=validate(input("Enter Employee Comp Name:"))
            #Design the Query
            iq="insert into employee values(%d,'%s',%f,'%s')"
            cur.execute(iq %(eno,empname,sal,cname))
            con.commit()
            print("-" * 50)
            print("{} Employee Record Inserted Successfully--Verify".format(cur.rowcount))
            print("-"*50)
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this Program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle DB: ",db)
        except ValueError:
            print("Don't Enter alnums, strs and symbols for empno and Salary")
        except InvalidNameError:
            print("Don't enter Invalid Names for Emp Name and Comp Name")
#Main Program
recordinsert() # Function Call
