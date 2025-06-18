#Program for Updating sal and Comp Name of Employee Based on Emp Name
#OracleRecordUpdateEx1.py
import oracledb as orc
def updaterecord():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        uq="update employee set sal=sal+sal*50/100,compname='wipro' where eno=500"
        cur.execute(uq)
        con.commit()
        if(cur.rowcount>0):
            print("{} Employee Record Updated".format(cur.rowcount))
        else:
            print("Employee Record does not exist")
    except orc.DatabaseError as db:
        print("Problem in Oarcle DB: ",db)
#Main program
updaterecord() # Function Call