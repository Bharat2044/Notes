#Program for Demonstrating Class Level Method
#ClassLevelMethodEx5.py
class Student:
   @classmethod
   def getcrs(cls):
       Student.crs = "Python"  # Class Level Data Member
   @classmethod
   def getaddr(cls):
       cls.getcrs() # Calling Class Level method w.r.t cls
       cls.addr="HYDERABAD"  # Class Level Data Member
   def  getstudentData(self): # Instance Method
       self.sno=int(input("Enter Student Number:"))
       self.name=input("Enter Student Name:")
       self.marks=float(input("Enter Student Marks:"))
   def dispstuddata(self):
       print("-"*50)
       print("Student Details")
       print("-" * 50)
       print("Student Number:{}".format(self.sno))
       print("Student Name:{}".format(self.name))
       print("Student Marks:{}".format(self.marks))
       self.getcrs()  # Calling Instance method w.r.t self
       self.getaddr()  # Calling Instance method w.r.t self
       print("Student Course=", Student.crs)
       print("Student Addr=", Student.addr)
       print("-" * 50)

#Main Program
s=Student() # Create an Object
s.getstudentData() # Calling Instance method w.r.t Obect Name
s.dispstuddata()# Calling Instance method w.r.t Object Name
