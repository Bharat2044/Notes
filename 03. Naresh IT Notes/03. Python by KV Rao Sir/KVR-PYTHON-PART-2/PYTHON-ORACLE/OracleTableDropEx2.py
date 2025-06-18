#Program for Removing the Table from Oracle Database
#OracleTableDropEx2.py
import oracledb as orc
def removetable():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        tabname=input("Enter table to drop:")
        cur.execute("drop table %s" %tabname)
        print("Table Dropped Sucessfully-verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB: ",db)

#Main Program
removetable()