#EmployeeDatabaseEx1.py
import mysql.connector
class Employee:
    def getempvalues(self):
        self.eno = int(input("Enter Employee Number:"))
        self.name = input("Enter Employee Name:")
        self.sal = float(input("Enter Employee Salary:"))
    def saveemprecord(self):
        try:
            con=mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root",
                                database="7ambatch")
            cur=con.cursor()
            #Query
            iq="insert into emp values(%d,'%s',%f)"
            cur.execute(iq %(self.eno,self.name,self.sal))
            con.commit()
            print("{} Emp Record Inserted Successfully".format(cur.rowcount))
        except mysql.connector.DatabaseError as db:
            print("Problem in Database: ",db)

#Main program
eo=Employee()
eo.getempvalues()
eo.saveemprecord()
