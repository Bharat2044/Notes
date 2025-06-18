#Program for Inserting Record in employee Table
#OracleInsertRecordEx1.py
import oracledb as orc
def recordinsert():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        iq="insert into employee values(225,'Ricthe',4.7,'Bell Labs')"
        cur.execute(iq)
        con.commit()
        print("Employee Record Inserted Sucessfully--verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB: ",db)
#Main Program
recordinsert() # Function Call
