#Program for demonstrating Creating a Table
#OracleTableCreateEx2.py<---File Name and Module Name
import oracledb as orc # Step-1
def tablecreate():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4--
        tc=input("Enter DDL Query for Creating a Table in Oracle:")
        cur.execute(tc)
        print("Table Created Sucessfully in Oracle DB--Verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB: ",db)
#Main Program
tablecreate()  # Function call

