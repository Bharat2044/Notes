#SISViewRecords.py<---File and Module Name
import mysql.connector
def viewrecords():
    try:
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="root",
                                      database="7ambatch")
        cur=con.cursor()
        #Query for Reading the Records
        cur.execute("select * from student")
        #Get the Records by using fetchall()
        print("-"*50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t")
            print()
        print("-" * 50)
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL DB:",db)

