#Program for displaying all the records along with Column Names by accepting the table name from KBD
#TableRecords.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        cur.execute("select * from %s" %input("Enter Table Name:"))
        # Code for Getting the Col names
        columnsinfo=cur.description
        print("=" * 50)
        for colname in [coltpl[0] for coltpl in cur.description]:
            print(colname,end="\t")
        print()
        print("="*50)
        #Code for Getting the Records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t")
            print()
        print("=" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#Main Program
selectrecords()