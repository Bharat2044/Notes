#Program for Demonstrating Class Level Method
#ClassLevelMethodEx2.py
class Student:
   @classmethod
   def getcrs(cls):
       Student.crs = "Python"  # Class Level Data Member
   @classmethod
   def getaddr(cls):
       cls.addr="HYDERABAD"  # Class Level Data Member
#Main Program
Student.getcrs() # Calling Instance Method w.r.t Class Name
Student.getaddr() # Calling Instance Method w.r.t Class Name
print("Student Course=",Student.crs)
print("Student Addr=",Student.addr)

