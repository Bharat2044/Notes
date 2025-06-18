#Program for Reading OR GGetting  the records of any table
#OracleRecordSelectEx3.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Query for Reading the Records
        sq="select * from employee order by name asc"
        cur.execute(sq)
        #Get the Records by using fetchall()
        print("-"*50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t")
            print()
        print("-" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#Main Program
selectrecords()