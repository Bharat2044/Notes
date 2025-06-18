#Program for Demonstrating Static Method
#StaticMethodEx3.py
class Student:
    def getstuddata(self):
        self.sno=int(input("Enter Student  Number:"))
        self.name =input("Enter Student  Name:")
        self.marks=float(input("Enter Student  Marks:"))
class Employee:
    def getempdata(self):
        self.eno=int(input("Enter Employee  Number:"))
        self.name =input("Enter Employee  Name:")
        self.sal=float(input("Enter Employee Salary:"))
class Teacher:
    def getteacherdata(self):
        self.tno=int(input("Enter Teacher  Number:"))
        self.name =input("Enter Teacher Name:")
        self.marks=input("Enter Teacher  Subject:")
        self.exp=int(input("Enter Teacher  Exp:"))
class Hyd:
    @classmethod
    def getobjectdata(cls,objdata,objinfo):
        cls.dispobjectdata(objdata,objinfo) # Calling static Method w.r.t cls

    @staticmethod
    def dispobjectdata(objdata,objinfo):
        print("-"*50)
        print("{} Object Information".format(objinfo))
        print("-" * 50)
        for k,v in objdata.__dict__.items():
            print("\t{}--->{}".format(k,v))
        print("-"*50)

#Main Program
s=Student()
e=Employee()
t=Teacher()
s.getstuddata()
print("---------------------------------")
e.getempdata()
print("---------------------------------")
t.getteacherdata()
#Calling Class Method of Class
Hyd.getobjectdata(s,"Student") # Calling static Method w.r.t Class Name
Hyd.getobjectdata(e,"Employee") # Calling static Method w.r.t Class Name
Hyd.getobjectdata(t,"Teacher") # Calling static Method w.r.t Class Name
