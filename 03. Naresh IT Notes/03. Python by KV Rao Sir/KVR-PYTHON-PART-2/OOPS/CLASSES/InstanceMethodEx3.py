#Program for Demonstrating Instance Method
#InstanceMethodEx2.py
class Student:
    crs="PYTHON" # Here crs is called Class Level Data Member
    def getstuddata(self,objinfo):
        print("-"*50)
        self.sno=int(input("Enter {} Student Number:".format(objinfo)))
        self.name=input("Enter {} Student Name:".format(objinfo))
        self.marks=float(input("Enter {} Student Marks:".format(objinfo)))
        print("-" * 50)
        self.dispstuddata(objinfo)#Calling instance method w.r.t self
    def dispstuddata(self,objinfo):
        print("-"*50)
        print("{} Student Details".format(objinfo))
        print("-" * 50)
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("\tSTUDENT COURSE:{}".format(self.crs))
        #OR print("\tSTUDENT COURSE:{}".format(Student.crs))
        print("-" * 50)
#Main Program
s1=Student()
s2=Student()
#read and display First Student Data
s1.getstuddata("First")
s2.getstuddata("Second")
