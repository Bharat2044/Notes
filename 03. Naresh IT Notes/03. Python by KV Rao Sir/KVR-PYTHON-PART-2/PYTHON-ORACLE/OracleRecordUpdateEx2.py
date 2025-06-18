#Program for Updating sal and Comp Name of Employee Based on Emp Name
#OracleRecordUpdateEx2.py
import oracledb as orc
def updaterecord():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/orcl")
            cur=con.cursor()
            #Accept Employee details
            empno=int(input("Enter Employee Number for Updating Sal and Comp Name:"))
            empsal=float(input("Enter Employee New Salary:"))
            cname=input("Enter Employee New Comp Name:")
            #Query with Dynamic Values
            uq="update employee set sal=%f,compname='%s' where eno=%d"
            cur.execute(uq %(empsal,cname,empno))
            con.commit()
            if(cur.rowcount>0):
                print("{} Employee Record Updated".format(cur.rowcount))
            else:
                print("Employee Record does not exist")
            print("-"*50)
            ch=input("Do u want to update another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for Using This Program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oarcle DB: ",db)
        except ValueError:
            print("Don't enter alnum, str and symbols for emp number and Salary")

#Main program
updaterecord() # Function Call