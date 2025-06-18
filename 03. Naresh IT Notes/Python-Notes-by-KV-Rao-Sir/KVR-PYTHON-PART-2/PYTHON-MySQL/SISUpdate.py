#SISUpdate.py<---File Name and Module Name
import mysql.connector
def updaterecord():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="7ambatch")
            cur=con.cursor()
            #Accept Employee details
            stno=int(input("Enter Student Number for Updating Marks and Name:"))
            marks=float(input("Enter Student Marks:"))
            sname=input("Enter Student Name:")
            #Query with Dynamic Values
            uq="update student set marks=%f,name='%s' where sno=%d"
            cur.execute(uq %(marks,sname,stno))
            con.commit()
            if(cur.rowcount>0):
                print("{} Student Record Updated".format(cur.rowcount))
            else:
                print("Student Record does not exist")
            print("-"*50)
            ch=input("Do u want to update another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for Using This Program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB: ",db)
        except ValueError:
            print("Don't enter alnum, str and symbols for emp number and Salary")

