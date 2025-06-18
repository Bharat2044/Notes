#Program for Deleting the Record from employee Table
#OracleDeleteRecordEx1.py
import oracledb as orc
def deleterecord():
    try:
        con = orc.connect("system/tiger@localhost/orcl")
        cur = con.cursor()
        dq="delete from employee where eno=150"
        cur.execute(dq)
        con.commit()
        if(cur.rowcount>0):
            print("{} Employee Record Deleted".format(cur.rowcount))
        else:
            print("Employee Record Does not Exist")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main program
deleterecord()