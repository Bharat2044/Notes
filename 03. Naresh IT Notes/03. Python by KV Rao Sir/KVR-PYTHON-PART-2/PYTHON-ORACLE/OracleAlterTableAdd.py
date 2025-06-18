#Program for Demonstrating adding the Column name to Employee Table
#OracleAlterTableAdd.py
import oracledb as orc
def altertable():
    try:
        con=orc.connect("system/tiger@127.0.0.1/orcl")
        cur=con.cursor()
        aq="alter table employee add(compname varchar2(10) )"
        cur.execute(aq)
        print("Table Altered--verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#Main Program
altertable() # Function Call