#Program for Deleting the Record from employee Table
#SISDeleteEx.py<----File Name and Module Name
import mysql.connector
def deleterecord():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="7ambatch")
            cur = con.cursor()
            #Accept employee Number from KBD
            stno=int(input("Enter Student Number:"))
            cur.execute("delete from student where sno=%d" %stno)
            con.commit()
            if(cur.rowcount>0):
                print("{} Student Record Deleted".format(cur.rowcount))
            else:
                print("Student Record Does not Exist")
            print("-"*50)
            ch=input("Do u want to delete another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB:",db)
        except ValueError:
            print("Don't Enter annums,strs and symbols for Employee Number")

