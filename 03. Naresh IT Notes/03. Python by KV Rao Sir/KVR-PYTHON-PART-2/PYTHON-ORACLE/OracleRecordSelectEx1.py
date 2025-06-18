#Program for Reading OR GGetting  the records of any table
#OracleRecordSelectEx1.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Query for Reading the Records
        sq="select * from employee"
        cur.execute(sq)
        #Get the Records by using fetchone()
        print("-"*50)
        while(True):
            rec = cur.fetchone()
            if(rec==None):
                break
            else:
                for val in rec:
                    print("{}".format(val),end="\t")
                print()
        print("-" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#Main Program
selectrecords()