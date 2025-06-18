#Program for Removing the Table from Oracle Database
#OracleTableDropEx1.py
import oracledb as orc
def removetable():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        cur.execute("drop table temp")
        print("Table Dropped Sucessfully-verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB: ",db)

#Main Program
removetable()