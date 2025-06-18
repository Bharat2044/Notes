#Student.py<---File Name and Module Name
import College as Ram
import mysql.connector
class Student(Ram.College):
    def getStudDet(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
        self.getCollDet() # Calling Base Class Method from Derived class Method
    def dispStudDet(self):
        self.dispCollDet() # Calling Base Class Method from Derived class Method
        print("-"*50)
        print("Student Details")
        print("-" * 50)
        print("Student Number:{}".format(self.sno))
        print("Student Name:{}".format(self.sname))
        print("Student Course:{}".format(self.crs))
        print("-" * 50)
    def saveData(self):
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="7ambatch")
            cur=con.cursor()
            #Prepare Query
            iq="insert into studinfo values(%d,'%s','%s','%s','%s','%s','%s') "
            cur.execute(iq %(self.sno,self.sname,self.crs,self.cname,self.cloc,self.uname,self.uloc))
            con.commit()
            print("Student Record Saved:")
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL: ",db)


