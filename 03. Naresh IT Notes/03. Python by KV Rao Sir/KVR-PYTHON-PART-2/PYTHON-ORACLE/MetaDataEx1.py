#Program for Obtaining Column Names of Table
#MetaDataEx1.py
import oracledb as orc
def selectcolnames():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        cur.execute("select * from employee")
        columnsinfo=cur.description
        #Here description is a pre-defined attribute present in cursor object and
        #It gives Meta Data ( Columns Information )
        print("=" * 50)
        for coltpl in columnsinfo:
            print(coltpl[0],end="\t")
        print()
        print("="*50)
        #Lots of Code
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#Main Program
selectcolnames()