#Program for demonstrating Creating a Table
#OracleTableCreateEx1.py
import oracledb as orc # Step-1
try:
    con=orc.connect("system/tiger@localhost/orcl") # Step-2
    cur=con.cursor() # Step-3
    #Step-4--
    tc="create table teacher(tno number(2) primary key, tname varchar2(10) not null, sal number(6,2) not null)"
    cur.execute(tc)
    print("Table Created Sucessfully in Oracle DB--Verify")
except orc.DatabaseError as db:
    print("Problem in Oracle DB: ",db)


