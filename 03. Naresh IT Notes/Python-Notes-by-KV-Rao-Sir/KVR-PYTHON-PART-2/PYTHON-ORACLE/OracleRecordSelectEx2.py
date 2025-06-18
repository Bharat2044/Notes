#Program for Reading OR GGetting  the records of any table
#OracleRecordSelectEx2.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Query for Reading the Records
        sq="select * from employee"
        cur.execute(sq)
        #Get the Records by using fetchmany()
        print("-"*50)
        records=cur.fetchmany(4)
        for record in records:
            for val in record:
                print("{}".format(val),end="\t")
            print()
        print("-" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#Main Program
selectrecords()