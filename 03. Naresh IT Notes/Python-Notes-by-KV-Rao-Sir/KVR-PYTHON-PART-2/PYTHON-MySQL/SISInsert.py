#SISInsert.py<--File Name and Module Name
import mysql.connector
def recordinsert():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="7ambatch")
            cur=con.cursor()
            #Accept employees values from KBD
            print("-" * 50)
            sno=int(input("Enter Student Number:"))
            name=input("Enter Student Name:")
            marks=float(input("Enter Student Marks:"))

            #Design the Query
            iq="insert into student values(%d,'%s',%f)"
            cur.execute(iq %(sno,name,marks))
            con.commit()
            print("-" * 50)
            print("Student Record Inserted Successfully--Verify")
            print("-"*50)
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this Program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB: ",db)

