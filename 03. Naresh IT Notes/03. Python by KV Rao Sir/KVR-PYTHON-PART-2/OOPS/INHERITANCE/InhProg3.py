#InhProg3.py
class University:
    def getUnivDet(self):
        self.uname=input("Enter Univesity Name:")
        self.uloc=input("Enter University Location:")
    def dispUnivDet(self):
        print("-"*50)
        print("University Details")
        print("-" * 50)
        print("University Name:{}".format(self.uname))
        print("University Location:{}".format(self.uloc))
        print("-" * 50)
class College(University):
    def getCollDet(self):
        self.cname=input("Enter College Name:")
        self.cloc=input("Enter College Location:")
        self.getUnivDet()# Calling Base Class Method from Derived class Method
    def dispCollDet(self):
        self.dispUnivDet()# Calling Base Class Method from Derived Class Method
        print("-" * 50)
        print("College Details")
        print("-" * 50)
        print("College Name:{}".format(self.cname))
        print("College Location:{}".format(self.cloc))
        print("-" * 50)
class Student(College):
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
#Main Program
s=Student()
s.getStudDet()
s.dispStudDet()