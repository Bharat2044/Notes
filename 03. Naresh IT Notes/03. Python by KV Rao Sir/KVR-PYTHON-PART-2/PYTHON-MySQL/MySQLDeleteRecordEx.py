#Program for Deleting the Record from employee Table
#OracleDeleteRecordEx3.py
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
            empno=int(input("Enter Employee Number:"))
            cur.execute("delete from employee where eno=%d" %empno)
            con.commit()
            if(cur.rowcount>0):
                print("{} Employee Record Deleted".format(cur.rowcount))
            else:
                print("Employee Record Does not Exist")
            print("-"*50)
            ch=input("Do u want to delete another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB:",db)
        except ValueError:
            print("Don't Enter annums,strs and symbols for Employee Number")

#Main program
deleterecord()