#Program for Demonstrating Modifying the Column sizes of Employee Table
#OracleAlterTableModify.py
import oracledb as orc
def altertable():
    try:
        con=orc.connect("system/tiger@127.0.0.1/orcl")
        cur=con.cursor()
        aq="alter table employee modify(eno number(3),name varchar2(15))"
        cur.execute(aq)
        print("Table Altered--verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
altertable() # Function Call