#SISSelect.py<----File and Module Name
import mysql.connector
def selectrecords():
    try:
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="root",
                                      database="7ambatch")
        cur=con.cursor()
        #Query for Reading the Records
        cur.execute("select * from student where sno=%d"%(int(input("Enter Student Number"))))
        #Get the Records by using fetchall()
        print("-"*50)
        record=cur.fetchone()
        if(record==None):
            print("Student Record Does Exist")
        else:
            for val in record:
                print("{}".format(val),end="\t")
                print()
        print("-" * 50)
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL DB:",db)

