#Program for displaying all the records along with Column Names by accepting the table name from KBD
#MySQLSelectRecordsWithColNames.py
import mysql.connector
def selectrecords():
    try:
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="root",
                                      database="7ambatch")
        cur=con.cursor()
        cur.execute("select * from %s" %input("Enter Table Name:"))
       #Code for Getting the Records
        records=cur.fetchall()
        if(len(records)==0):
            print("Table Does not Contain any Record")
        else:
            # Code for Getting the Col names
            columnsinfo = cur.description
            print("=" * 50)
            for colname in [coltpl[0] for coltpl in cur.description]:
                print(colname, end="\t")
            print()
            print("=" * 50)
            #get the records
            for record in records:
                for val in record:
                    print("{}".format(val),end="\t")
                print()
            print("=" * 50)
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL DB:",db)
#Main Program
selectrecords()
