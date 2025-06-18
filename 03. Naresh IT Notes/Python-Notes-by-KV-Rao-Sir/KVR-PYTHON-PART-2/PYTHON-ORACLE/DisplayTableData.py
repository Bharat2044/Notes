#Program for displaying all the records along with Column Names
#DisplayTableData.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        cur.execute("select * from employee")
        # Code for Getting the Col names
        columnsinfo=cur.description
        print("=" * 50)
        for coltpl in columnsinfo:
            print(coltpl[0],end="\t")
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