#Program for Reading OR GGetting  the records of any table
#MySQLRecordSelectEx.py
import mysql.connector
def selectrecords():
    try:
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="root",
                                      database="7ambatch")
        cur=con.cursor()
        #Query for Reading the Records
        sq="select * from employee"
        cur.execute(sq)
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
#Main Program
selectrecords()